import os
from django.conf import settings
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.text import slugify

from main.models import Experience, Coursework
from main.forms import ExperienceForm


def show_main(request):
    education_list = [
        {
            "period": "2025 — Present",
            "institution": "Universitas Indonesia",
            "degree": "Undergraduate of Information Systems",
        },
        {
            "period": "2022 — 2025",
            "institution": "SMA Negeri 13 Jakarta",
            "degree": "High School Diploma",
        },
    ]

    interests_list = [
        {
            "title": "Auditing",
            "description": (
                "As someone who loves administrative work, I am naturally drawn to the world of auditing, "
                "considering I am an IS student: IT auditing. There is something deeply satisfying about "
                "ensuring that IT systems are accurate and that organizations are operating efficiently "
                "and ethically."
            ),
        },
        {
            "title": "Marine Sciences",
            "description": (
                "I'm an island girl at heart, well at least when I'm on vacation. I'm deeply interested in "
                "marine sciences and hope to contribute to ocean conservation with IS."
            ),
        },
        {
            "title": "Business",
            "description": (
                "Although I realize I am not in business major entirely, I have always been interested "
                "in the world of business, management, and how technology can be used to improve business "
                "processes."
            ),
        },
        {
            "title": "Story-Heavy Games",
            "description": (
                "Unrelated to any of my jobs, I really enjoy playing story-heavy games, such as Subnautica, "
                "Red Dead Redemption 2, and other major AAA games."
            ),
        },
    ]

    context = {
        "name": "Balqis Raihana",
        "npm": "2506625981",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            """A highly flexible generalist who enjoys taking on different kinds of work, especially 
            roles that involve organizing, coordinating, and solving day-to-day problems. I enjoy being 
            someone people can come to with questions, which is why I particularly value my experiences 
            in teaching and administrative roles. Alongside this, I am developing my interest in Data 
            Science and analytical problem-solving, with the long-term goal of exploring IT Audit at the 
            intersection of technology, data, processes, and business."""
        ),
        "education_list": education_list,
        "interests_list": interests_list,
        "coursework_list": Coursework.objects.all(),
    }
    return render(request, "index.html", context)


def show_experience(request):
    json_response = get_experience_json(request)
    experiences = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    experience_list = [item.object for item in experiences]
    title_query = request.GET.get("title", "").strip()
    category_query = request.GET.get("category", "").strip().lower()

    context = {
        "name": "Balqis Raihana",
        "experience_list": experience_list,
        "title_query": title_query,
        "category_query": category_query,
        "coursework_list": Coursework.objects.all(),
    }
    return render(request, "experience.html", context)


def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New experience successfully added!")
        return redirect("main:show_experience")

    context = {
        "name": "Balqis Raihana",
        "form": form,
        "coursework_list": Coursework.objects.all(),
    }
    return render(request, "experience_form.html", context)


def edit_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)
    form = ExperienceForm(request.POST or None, instance=experience)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Experience successfully updated!")
        return redirect("main:show_experience")

    context = {
        "name": "Balqis Raihana",
        "form": form,
        "experience": experience,
        "is_edit": True,
        "coursework_list": Coursework.objects.all(),
    }
    return render(request, "experience_form.html", context)


def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    category_query = request.GET.get("category", "").strip().lower()
    experiences = Experience.objects.all().order_by("-started_at")

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)
    if category_query and category_query != "all":
        experiences = experiences.filter(category=category_query)

    experiences_json = serializers.serialize("json", experiences)
    return HttpResponse(experiences_json, content_type="application/json")


def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience successfully deleted!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")


def show_coursework(request):
    context = {
        "name": "Balqis Raihana",
        "coursework_list": Coursework.objects.all(),
    }
    return render(request, "coursework.html", context)


def get_course_journal_images(course):
    coursework_img_dir = os.path.join(settings.BASE_DIR, "static", "img", "coursework")
    if not os.path.exists(coursework_img_dir):
        return []

    pk_str = str(course.id)
    slug_name = slugify(course.name)

    allowed_exts = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".svg"}
    found_images = []

    # 1. Check folder matching pk or slug
    folder_candidates = [
        os.path.join(coursework_img_dir, pk_str),
        os.path.join(coursework_img_dir, slug_name),
    ]
    for folder in folder_candidates:
        if os.path.isdir(folder):
            folder_name = os.path.basename(folder)
            for fname in sorted(os.listdir(folder)):
                ext = os.path.splitext(fname)[1].lower()
                if ext in allowed_exts:
                    found_images.append({
                        "url": f"/static/img/coursework/{folder_name}/{fname}",
                        "caption": os.path.splitext(fname)[0].replace("-", " ").replace("_", " ").title(),
                    })
            if found_images:
                return found_images

    # 2. Check files directly in static/img/coursework starting with slug or pk
    for fname in sorted(os.listdir(coursework_img_dir)):
        fpath = os.path.join(coursework_img_dir, fname)
        if os.path.isfile(fpath):
            ext = os.path.splitext(fname)[1].lower()
            if ext in allowed_exts:
                name_without_ext = os.path.splitext(fname)[0]
                if name_without_ext.startswith(slug_name) or name_without_ext.startswith(pk_str):
                    caption = name_without_ext.replace(slug_name, "").replace(pk_str, "").strip("-_")
                    found_images.append({
                        "url": f"/static/img/coursework/{fname}",
                        "caption": caption.replace("-", " ").replace("_", " ").title() or course.name,
                    })

    return found_images


def show_coursework_detail(request, pk):
    course = get_object_or_404(Coursework, pk=pk)
    journal_images = get_course_journal_images(course)
    context = {
        "name": "Balqis Raihana",
        "course": course,
        "coursework_list": Coursework.objects.all(),
        "journal_images": journal_images,
    }
    return render(request, "coursework_detail.html", context)
