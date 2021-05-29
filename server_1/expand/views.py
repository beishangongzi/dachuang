from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.templatetags.rest_framework import data

from .models import Introduction, Image
import socket
# Create your views here.

def get_intro(request):
    data = request.GET.get("value")
    res = Introduction.objects.filter(id__icontains=data)
    s = [r.id for r in res][:2]
    print(s)
    return JsonResponse({"data": s})

def get_text(request):
    data = request.GET.get("value")
    print(data)
    res = Introduction.objects.get(id=data).text
    return JsonResponse({"data": res})

def get_image(request):
    data = request.GET.get("value")
    img = Image.objects.filter(img__contains=data)[0:3]
    dic = dict(zip([i.name for i in img ], [i.img.url for i in img]))
    ls = [i.img.url for i in img]
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    ip = s.getsockname()[0]
    s.close()
    ls = list(map(lambda x: "http://" + ip+ ":8000" + x, ls))
    return JsonResponse({"src": ls})

def get_list(request):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    ip = s.getsockname()[0]
    s.close()
    ls = Introduction.objects.all()
    data = []
    for l in ls:
        dy = l.id
        text = l.text[:35] + "..."
        img_url = Image.objects.filter(img__contains=dy)[0].img.url
        img = "http://" + ip + ":8000" + img_url
        name = Image.objects.filter(img__contains=dy)[0].name.split("-")[5]
        data.append([dy, text, img, name])
    print("dd")
    return JsonResponse({"data": data})
