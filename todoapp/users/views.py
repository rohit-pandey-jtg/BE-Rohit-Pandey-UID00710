from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .serializers import UserApiSerializer
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny

from rest_framework.response import Response
from rest_framework import status

class UserRegistrationAPIView(APIView):
    """
        success response format
         {
           first_name: "",
           last_name: "",
           email: "",
           date_joined: "",
           "token"
         }
    """
    permission_classes = [AllowAny]

    def get(self, request):
        return Response(
            {"message" : "Hit the users/views GET method"},
            status = status.HTTP_200_OK
        )
    def post(self, request, *args, **kwargs):
        serializer = UserApiSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        token_obj, _ = Token.objects.get_or_create(user=user)
        return Response(
            {
              "first_name" : user.first_name,
              "last_name" : user.last_name,
              "email" : user.email,
              "date_joined" : user.date_joined,
              "token" : token_obj.key
            },
            status=status.HTTP_201_CREATED
        )

class UserLoginAPIView(APIView):
    """
        success response format
         {
           auth_token: ""
         }
    """
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(email = email, password = password)

        if not user:
            return Response(
                {
                    "error" : "Invalid Creds"
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

        token_obj,_ = Token.objects.get_or_create(user = user)
        return Response(
            {
                "auth_token" :token_obj.key
            },
            status=status.HTTP_200_OK
        )