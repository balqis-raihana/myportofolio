from django.urls import path
from main import api_views

app_name = "api"

urlpatterns = [
    # Projects / Experience Endpoints (Tutorial 07)
    path("projects/", api_views.project_list, name="project-list"),
    path("projects/<uuid:project_id>/", api_views.project_detail, name="project-detail"),
    path("projects/<uuid:project_id>/star/", api_views.project_star, name="project-star"),

    # Coursework Endpoints (Individual Assignment 6)
    path("coursework/", api_views.coursework_list, name="coursework-list"),
    path("coursework/<uuid:coursework_id>/", api_views.coursework_detail, name="coursework-detail"),
    path("coursework/<uuid:coursework_id>/star/", api_views.coursework_star, name="coursework-star"),
]
