"""home URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:

"""

from django.urls import path
from . import views
urlpatterns = [
    path("booth1/", views.booth1, name="booth1"),
    path("booth2/", views.booth2, name="booth2"),
    path("booth3/", views.booth3, name="booth3"),
]
