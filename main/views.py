from django.shortcuts import render, get_object_or_404

from main.models import Experience, Coursework


def show_main(request):
    context = {
        "name": "Balqis Raihana",
        "npm": "2506625981",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            """I consider myself a multidisciplinary learner who is comfortable working across technical, 
               analytical, and organizational domains. While I continue to develop expertise in specific 
               areas, I am driven by curiosity, adaptability, and a desire to keep learning new things."""
        ),
        "coursework_list": Coursework.objects.all(),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Balqis Raihana",
        "experience_list": Experience.objects.all(),
        "coursework_list": Coursework.objects.all(),
    }
    return render(request, "experience.html", context)


def show_coursework(request):
    context = {
        "name": "Balqis Raihana",
        "coursework_list": Coursework.objects.all(),
    }
    return render(request, "coursework.html", context)


def show_coursework_detail(request, pk):
    course = get_object_or_404(Coursework, pk=pk)
    context = {
        "name": "Balqis Raihana",
        "course": course,
        "coursework_list": Coursework.objects.all(),
    }
    return render(request, "coursework_detail.html", context)