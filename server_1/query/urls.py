from .views import getImage
from django.urls import include, path

urlpatterns = [
    path('', getImage)
]
