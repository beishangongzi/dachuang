from django.urls import path
from .views import get_intro, get_text,get_image, get_list

urlpatterns = [
    path("list/", get_list),
    path("image/", get_image),
    path("text/", get_text),
    path("", get_intro),

]