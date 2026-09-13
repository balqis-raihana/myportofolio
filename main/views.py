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
        "experience_list": Experience.objects.all().order_by('-started_at'),
        "coursework_list": Coursework.objects.all(),
    }
    return render(request, "experience.html", context)


def show_coursework(request):
    context = {
        "name": "Balqis Raihana",
        "coursework_list": Coursework.objects.all(),
    }
    return render(request, "coursework.html", context)


import os
from django.conf import settings
from django.utils.text import slugify

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
