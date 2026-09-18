from django.urls import path

from main.views import (
    show_main,
    show_experience,
    create_experience,
    edit_experience,
    get_experience_json,
    delete_experience,
    show_coursework,
    show_coursework_detail,
    create_coursework,
    edit_coursework,
    delete_coursework,
    get_coursework_json,
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("experience/add/", create_experience, name="create_experience"),
    path("experience/<uuid:experience_id>/edit/", edit_experience, name="edit_experience"),
    path("experience/<uuid:experience_id>/delete/", delete_experience, name="delete_experience"),
    path("api/experience/", get_experience_json, name="get_experience_json"),
    path("coursework/", show_coursework, name="show_coursework"),
    path("coursework/add/", create_coursework, name="create_coursework"),
    path("coursework/<uuid:coursework_id>/edit/", edit_coursework, name="edit_coursework"),
    path("coursework/<uuid:coursework_id>/delete/", delete_coursework, name="delete_coursework"),
    path("api/coursework/", get_coursework_json, name="get_coursework_json"),
    path("coursework/<uuid:pk>/", show_coursework_detail, name="show_coursework_detail"),
]
