"""
URL configuration for myportofolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("main.api_urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("contacts/", include("contacts.urls")),
    path("", include("main.urls")),
]
