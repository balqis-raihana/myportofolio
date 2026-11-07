from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from main.models import Experience, Coursework
from main.permissions import IsPortfolioOwnerOrReadOnly, IsPortfolioOwnerOrEditorOrReadOnly
from main.serializers import ExperienceSerializer, CourseworkSerializer


# ==============================================================================
# Experience / Projects API (Tutorial 07)
# ==============================================================================

@api_view(["GET", "HEAD", "POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrReadOnly])
def project_list(request):
    if request.method in ("GET", "HEAD"):
        experiences = Experience.objects.prefetch_related("starred_by").order_by("-started_at", "id")
        title = request.query_params.get("title", "").strip()
        category = request.query_params.get("category", "").strip().lower()

        if title:
            experiences = experiences.filter(title__icontains=title)
        if category and category != "all":
            experiences = experiences.filter(category=category)

        serializer = ExperienceSerializer(
            experiences,
            many=True,
            context={"request": request},
        )
        return Response(serializer.data)

    serializer = ExperienceSerializer(data=request.data, context={"request": request})
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "HEAD", "PUT", "PATCH", "DELETE"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrReadOnly])
def project_detail(request, project_id):
    experience = get_object_or_404(
        Experience.objects.prefetch_related("starred_by"),
        pk=project_id,
    )

    if request.method in ("GET", "HEAD"):
        serializer = ExperienceSerializer(experience, context={"request": request})
        return Response(serializer.data)

    if request.method == "DELETE":
        experience.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    serializer = ExperienceSerializer(
        experience,
        data=request.data,
        partial=request.method == "PATCH",
        context={"request": request},
    )
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(["POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def project_star(request, project_id):
    experience = get_object_or_404(Experience, pk=project_id)
    if experience.starred_by.filter(pk=request.user.pk).exists():
        experience.starred_by.remove(request.user)
    else:
        experience.starred_by.add(request.user)
    serializer = ExperienceSerializer(experience, context={"request": request})
    return Response(serializer.data)


# ==============================================================================
# Coursework API (Individual Assignment 6)
# ==============================================================================

@api_view(["GET", "HEAD", "POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def coursework_list(request):
    if request.method in ("GET", "HEAD"):
        coursework = Coursework.objects.prefetch_related("starred_by").order_by("name", "id")
        search_query = request.query_params.get("search", "").strip() or request.query_params.get("q", "").strip()
        category = request.query_params.get("category", "").strip().lower()

        if search_query:
            coursework = coursework.filter(name__icontains=search_query)
        if category and category != "all":
            coursework = coursework.filter(category__icontains=category)

        serializer = CourseworkSerializer(
            coursework,
            many=True,
            context={"request": request},
        )
        return Response(serializer.data)

    # POST create data (hanya superuser yang lolos permission IsPortfolioOwnerOrEditorOrReadOnly)
    serializer = CourseworkSerializer(data=request.data, context={"request": request})
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "HEAD", "PUT", "PATCH", "DELETE"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def coursework_detail(request, coursework_id):
    course = get_object_or_404(
        Coursework.objects.prefetch_related("starred_by"),
        pk=coursework_id,
    )

    if request.method in ("GET", "HEAD"):
        serializer = CourseworkSerializer(course, context={"request": request})
        return Response(serializer.data)

    if request.method == "DELETE":
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    serializer = CourseworkSerializer(
        course,
        data=request.data,
        partial=request.method == "PATCH",
        context={"request": request},
    )
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(["POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def coursework_star(request, coursework_id):
    course = get_object_or_404(Coursework, pk=coursework_id)
    if course.starred_by.filter(pk=request.user.pk).exists():
        course.starred_by.remove(request.user)
    else:
        course.starred_by.add(request.user)
    serializer = CourseworkSerializer(course, context={"request": request})
    return Response(serializer.data)
