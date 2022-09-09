import json
import logging
from django.http import JsonResponse
from .models import User
from django.contrib.auth import authenticate

logging.basicConfig(filename='user_views.log', filemode='a', level=logging.DEBUG)


def registration(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            User.objects.create_user(username=data.get("username"),
                                     password=data.get("password"),
                                     email=data.get("email"),
                                     phone_number=data.get("phone_number"),
                                     location=data.get("location"))
            return JsonResponse({"message": "Data saved successfully"})
        return JsonResponse("Method not allowed")
    except Exception as e:
        logging.exception(e)
        return JsonResponse({"message": "Error occurred"})


def login(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            login_user = authenticate(username=data.get("username"), password=data.get("password").first())
            if login_user is not None:
                return JsonResponse({"message": f"User {login_user.username} successfully logged in"})
            else:
                return JsonResponse({"message": "Invalid Credentials"})
        return JsonResponse("Method not allowed")
    except Exception as e:
        logging.exception(e)
        return JsonResponse({"message": "Error occurred"})


def change_password(request):
    try:
        data = json.loads(request.body)
        user = User.objects.get(username=data.get('username'))
        user.set_password(data.get('new_password'))
        user.save()
        return JsonResponse({'message': 'Successfully change new password'})
    except Exception as e:
        print(e)
        return JsonResponse({})
