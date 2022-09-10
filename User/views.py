import json
import logging
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from django.contrib.auth import authenticate

logging.basicConfig(filename='user_views.log', filemode='a', level=logging.DEBUG)


class Registration(APIView):
    def post(self, request):
        try:
            data = json.loads(request.body)
            user_registration = User.objects.create_user(username=data.get("username"),
                                                         password=data.get("password"),
                                                         email=data.get("email"),
                                                         phone_number=data.get("phone_number"),
                                                         location=data.get("location"))
            user_registration.save()
            return Response({"message": "Data saved successfully"})
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


class ChangePassword(APIView):
    def post(self, request):
        try:
            data = json.loads(request.body)
            user = User.objects.get(username=data.get('username'))
            user.set_password(data.get('new_password'))
            user.save()
            return Response({'message': 'Successfully change new password'})
        except Exception as e:
            print(e)
            return Response({})
