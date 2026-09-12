from django.shortcuts import render

from main.models import Experience, Coursework


def show_main(request):
    context = {
        "name": "Balqis Raihana",
        "npm": "2506625981",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            """I consider myself a highly flexible generalist who enjoys taking on different 
            kinds of work, especially roles that involve organizing, coordinating, and solving 
            day-to-day problems. I enjoy being someone people can come to with questions, which 
            is why I particularly value my experiences in teaching and administrative roles. 
            Alongside this, I am developing my interest in Data Science and analytical problem-solving, 
            with the long-term goal of exploring IT Audit at the intersection of technology, data, 
            processes, and business."""
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Balqis Raihana",
        "experience_list": Experience.objects.all().order_by('-started_at'),
    }
    return render(request, "experience.html", context)

def show_coursework(request):
    context = {
        "name": "Balqis Raihana",
        "coursework_list": Coursework.objects.all(),
    }
    return render(request, "coursework.html", context)