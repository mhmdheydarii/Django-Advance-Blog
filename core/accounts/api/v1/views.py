from rest_framework import generics
from .serializers import (RegistrationsSerializers, CustomAuthTokenSerializer,
                        CustomTokenObtaiPairSerializer, ChangePasswordSerializer,
                        ProfileSerializer, ResendActivationSerializer)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from accounts.models import User, Profile
from django.shortcuts import get_object_or_404
from mail_templated import send_mail
from rest_framework_simplejwt.tokens import RefreshToken
import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidSignatureError, DecodeError
from django.conf import settings

class RegistrationApiView(generics.GenericAPIView):

    serializer_class = RegistrationsSerializers

    def post(self, request, *args, **kwargs):
        serializers = RegistrationsSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            email = serializers.validated_data['email']
            data = {
                'email': email
            }
            user_obj = get_object_or_404(User, email=email)
            token = self.get_tokens_for_user(user_obj)
            send_mail('email/activation-email.tpl', {'token':token}, 'mohammad@gmail.com', [email])
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)


class CustomObtainAuthToken(ObtainAuthToken):

    serializer_class = CustomAuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, 
                                           context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })


class CustomDiscardAuthToken(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# Custom JWT token 
class CustomTokenObtainPairView(TokenObtainPairView):

    serializer_class = CustomTokenObtaiPairSerializer

# Changing the password of account 
class ChangePasswordApiView(generics.GenericAPIView):

    model = User
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self, queryset=None):
        obj = self.request.user

        return obj
    
    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
                # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response({'detail':'password set succesfully'}, status=status.HTTP_200_OK)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Updating Profile account
class ProfileApiView(generics.RetrieveUpdateAPIView):

    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj
    
# sent verification email for user
class SentEmailView(generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
        self.email = 'raha@gmail.com'
        user_obj = get_object_or_404(User, email=self.email)
        token = self.get_tokens_for_user(user_obj)
        send_mail('email/hello.tpl', {'token':token}, 'mohammad@gmail.com', [self.email])
        return Response({'email sent'})
    
    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

class VerifyViewToken(APIView):

    def get(self, request, token, *args, **kwargs):
        try:
            token = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user_id = token.get('user_id')
        except ExpiredSignatureError:
            return Response({'detail':'ExpiredSignatureError'})
        except InvalidSignatureError:
            return Response({'detail':'invalid error'})
        except DecodeError:
            return Response({'detail': 'DecodeError'})
        
        user_obj = User.objects.get(pk = user_id)
        if user_obj.is_verified:
            return Response({"detail": "Your account has already been verified"})
        user_obj.is_verified = True
        user_obj.save()
        return Response({"detail": "your account verified successfully"})
    

class ResendVerifyApiView(generics.GenericAPIView):

    serializer_class = ResendActivationSerializer

    def post(self, request, *args, **kwargs):
        serializer = ResendActivationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_obj = serializer.validated_data['user']
        token = self.get_tokens_for_user(user_obj)
        send_mail('email/activation-email.tpl', {'token':token}, 'mohammad@gmail.com', [user_obj.email])
        return Response({"detail": "User activation resend successfully"})
        
        
    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)
