from rest_framework.generics import GenericAPIView
from .serializers import RegistrationsSerializers
from rest_framework.response import Response
from rest_framework import status


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
    