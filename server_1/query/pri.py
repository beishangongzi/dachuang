import torch
import numpy as np
import os
from PIL import Image
import torchvision.transforms as transforms
import re


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
    d = ['明-万历','明-嘉靖','明-宣德','明-成化','明-永乐','明-洪武','明-隆庆','清-乾隆', '清-康熙', '清-雍正']
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


if __name__ == '__main__':
    img = preProcess("./../static/images/search/swiper_image_3.png")
    pridict(img, None)
