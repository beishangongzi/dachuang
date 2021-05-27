from .views import getImage, requestImage
from django.urls import include, path

urlpatterns = [
    path("download", requestImage),
    path('', getImage),
]
