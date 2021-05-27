from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def getImage(request):
    image = request.FILES["image"]
    path = "/tmp/"
    with open(path + "3.png", "wb+") as f:
        f.write(image.read())
    return HttpResponse("3.png")
