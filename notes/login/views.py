from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User 
from django.http import JsonResponse
from django.core.exceptions import BadRequest


@csrf_exempt 
def auth(request):
    if request.method == "GET":
        return HttpResponse("Enter email and pass")    
    elif request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        if email and password:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                user = User(email=email, password=password)
            return JsonResponse({'token':'qewreqwreq'})

        raise BadRequest('Invalid email or password.')
   


