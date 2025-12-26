from rest_framework.generics import GenericAPIView
from .serializers import RegistrationsSerializers, CustomAuthTokenSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken


class RegistrationApiView(GenericAPIView):

    serializer_class = RegistrationsSerializers

    def post(self, request, *args, **kwargs):
        serializers = RegistrationsSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            data = {
                'email':serializers.validated_data['email']
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    

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
