from rest_framework import views
from .models import User 
from django.http import JsonResponse
from django.db import IntegrityError
from .cryptogtapher import Cryptographer


class AuthView(views.APIView):
    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")
        key = b'kpzky_nk07lDWu-PR6hYn6IrLuAGsOCfg8a1ngDCjDo='
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
