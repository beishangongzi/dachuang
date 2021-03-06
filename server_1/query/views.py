from django.http import HttpResponse, JsonResponse, StreamingHttpResponse
from django.shortcuts import render
from rest_framework.response import Response

import torch
import numpy as np
import os
from PIL import Image
import torchvision.transforms as transforms
import re
from expand.models import Introduction


def preProcess(image):
    img = Image.open(image)
    transform = transforms.Compose([transforms.Resize(256),  # 重置图像分辨率
                                    transforms.CenterCrop(224),  # 中心裁剪
                                    transforms.ToTensor(), ])
    img = img.convert("RGB")  # 如果是标准的RGB格式，则可以不加
    img = transform(img)
    img = img.unsqueeze(0)
    return img


def pridict(img: Image, modelPath: None):
    d = ['明万历','明嘉靖','明宣德','明成化','明永乐','明洪武','明隆庆','清乾隆', '清康熙', '清雍正']
    if modelPath is None:
        modelPath = 'model.pkl'
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = torch.load(modelPath)
    model = model.to(device)
    model.eval()  # 预测模式
    img = img.to(device)

    with torch.no_grad():
        py = model(img)
    _, predicted = torch.max(py, 1)  # 获取分类结果
    regex = re.compile(r'\d')
    classIndex_ = int(regex.search(str(predicted[0])).group())
    print('预测结果', d[classIndex_])
    return d[classIndex_]




# Create your views here.

def getImage(request):
    image = request.FILES["image"]
    path = "/tmp/"
    with open(path + "3.jpg", "wb+") as f:
        f.write(image.read())
        img = preProcess(image)
        res = pridict(img, "/media/andy/Data/dachuang/server_1/query/model.pkl")
        intro = Introduction.objects.get(id=res)
        text = intro.text
    return JsonResponse({"res": res, "text": text})


def requestImage(request):
    name = request.GET.get("name")
    path = 'static/images/search/'
    print(name)
    with open(path+name, 'rb') as f:
        return HttpResponse(f.read(), content_type='image/jpg')



