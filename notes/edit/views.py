from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt 
def edit(request):
    if request.method == "GET":
        return HttpResponse("Enter email and pass")    
    elif request.method == "POST":
        print(request.body)
        return HttpResponse("Success")    

