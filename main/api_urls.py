from django.urls import path
from rest_framework.authtoken import views as authtoken_views
from main import api_views

app_name = "api"

urlpatterns = [
    # Auth Endpoints (Tutorial 10)
    path("auth/token/", authtoken_views.obtain_auth_token, name="api_token_auth"),
    path("auth/logout/", api_views.api_logout, name="api_logout"),

    # Projects / Experience Endpoints (Tutorial 07)
    path("projects/", api_views.project_list, name="project-list"),
    path("projects/<uuid:project_id>/", api_views.project_detail, name="project-detail"),
    path("projects/<uuid:project_id>/star/", api_views.project_star, name="project-star"),

    # Coursework Endpoints (Individual Assignment 6)
    path("coursework/", api_views.coursework_list, name="coursework-list"),
    path("coursework/<uuid:coursework_id>/", api_views.coursework_detail, name="coursework-detail"),
    path("coursework/<uuid:coursework_id>/star/", api_views.coursework_star, name="coursework-star"),
]
