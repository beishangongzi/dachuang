from django.http import HttpResponse, JsonResponse, StreamingHttpResponse
from django.shortcuts import render
from rest_framework.response import Response


# Create your views here.

def getImage(request):
    image = request.FILES["image"]
    path = "/tmp/"
    with open(path + "3.jpg", "wb+") as f:
        f.write(image.read())
    return JsonResponse({"s": "dddd"})


def requestImage(request):
    name = request.GET.get("name")
    path = 'static/images/search/'
    print(name)
    with open(path+name, 'rb') as f:
        return HttpResponse(f.read(), content_type='image/jpg')



