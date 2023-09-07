from rest_framework import views
from .models import User 
from django.http import JsonResponse
from django.db import IntegrityError
from notes.cryptographer import Cryptographer
from django.conf import settings


class AuthView(views.APIView):
    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")
        key = settings.SECRET_KEY
        encrypted_pass = Cryptographer(key).encrypt(password)
        try:
            user = User.objects.get(email=email, password=encrypted_pass)
        except User.DoesNotExist:
            user = User(email=email, password=encrypted_pass)
            try:
                user.save()
            except IntegrityError:
                return JsonResponse({"error:": "Email is not unique"}, status=400)
        return JsonResponse({'token':user.token})
