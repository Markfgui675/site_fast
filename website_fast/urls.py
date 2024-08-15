
from django.contrib import admin
from django.urls import path
import website
from django.urls import include

urlpatterns = [
    path('', include('website.urls')),
]
