import json
import logging
from django.http import JsonResponse
from User.models import User

logging.basicConfig(filename='user_views.log', filemode='a', level=logging.DEBUG)


def registration(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            User.objects.create(username=data.get("username"),
                                password=data.get("password"),
                                email=data.get("email"),
                                phone_number=data.get("phone_number"),
                                location=data.get("location"))
            return JsonResponse({"message": "Data save successfully"})
        return JsonResponse("Method not allowed")
    except Exception as e:
        logging.exception(e)
        return JsonResponse({"message": "Error occurred"})


def login(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            login_user = User.objects.filter(username=data.get("username"), password=data.get("password").first())
            if login_user is not None:
                return JsonResponse({"message": f"User {login_user.username} successfully logged in"})
            else:
                return JsonResponse({"message": "Invalid Credentials"})
        return JsonResponse("Method not allowed")
    except Exception as e:
        logging.exception(e)
        return JsonResponse({"message": "Error occurred"})
