import json
import logging
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate

from .serializers import UserSerializer

logging.basicConfig(filename='user_views.log', filemode='a', level=logging.DEBUG)


class Registration(APIView):
    def post(self, request):
        try:
            # data = json.loads(request.body)
            # user_registration = User.objects.create_user(username=data.get("username"),
            #                                              password=data.get("password"),
            #                                              email=data.get("email"),
            #                                              phone_number=data.get("phone_number"),
            #                                              location=data.get("location"))
            user_serializer = UserSerializer(data=request.data)
            user_serializer.is_valid(raise_exception=True)
            user_serializer.save()
            return Response({"message": "Data saved successfully",
                             "data": user_serializer.data})
        except Exception as e:
            print(e)
            logging.exception(e)
            return Response({"message": "Error occurred"})


class Login(APIView):
    def post(self, request):
        try:
            data = json.loads(request.body)
            login_user = authenticate(username=data.get("username"), password=data.get("password"))
            if login_user is not None:
                return Response({"message": f"User {login_user.username} successfully logged in"})
            else:
                return Response({"message": "Invalid Credentials"})
        except Exception as e:
            logging.exception(e)
            return Response({"message": "Error occurred"})


