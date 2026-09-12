from django.urls import path

from main.views import show_main, show_experience, show_coursework, show_coursework_detail

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("coursework/", show_coursework, name="show_coursework"),
    path("coursework/<uuid:pk>/", show_coursework_detail, name="show_coursework_detail"),
]