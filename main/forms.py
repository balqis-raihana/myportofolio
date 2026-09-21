from django import forms
from django.forms import ModelForm, TextInput, Textarea, Select, URLInput, NumberInput, PasswordInput
from main.models import Experience, Coursework

class ExperienceForm(ModelForm):
    crud_password = forms.CharField(
        label="Admin Secret Key",
        widget=PasswordInput(
            attrs={
                "placeholder": "Enter secret key to authorize changes...",
                "autocomplete": "current-password",
            }
        ),
        required=False,
        help_text="Required if not authorized via header.",
    )

    class Meta:
        model = Experience
        fields = [
            "title",
            "company",
            "description",
            "category",
            "thumbnail",
        ]

        labels = {
            "title": "Title / Role",
            "company": "Company / Organization",
            "description": "Description",
            "category": "Category",
            "thumbnail": "Thumbnail URL (Optional)",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "e.g. Asisten Dosen PBP / UI/UX Intern",
                    "maxlength": 255,
                }
            ),
            "company": TextInput(
                attrs={
                    "placeholder": "e.g. Universitas Indonesia / Google",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Tell about your responsibilities and achievements...",
                    "rows": 4,
                }
            ),
            "category": Select(),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://... or leave blank",
                }
            ),
        }


class CourseworkForm(ModelForm):
    crud_password = forms.CharField(
        label="Admin Secret Key",
        widget=PasswordInput(
            attrs={
                "placeholder": "Enter secret key to authorize changes...",
                "autocomplete": "current-password",
            }
        ),
        required=False,
        help_text="Required if not authorized via header.",
    )

    class Meta:
        model = Coursework
        fields = [
            "name",
            "category",
            "description",
            "credits",
            "journal",
        ]

        labels = {
            "name": "Course Name",
            "category": "Category / Stream",
            "description": "Description",
            "credits": "Credits (SKS)",
            "journal": "Learning Journal (Optional)",
        }

        widgets = {
            "name": TextInput(
                attrs={
                    "placeholder": "e.g. Business Management / Pemrograman Berbasis Platform",
                    "maxlength": 255,
                }
            ),
            "category": TextInput(
                attrs={
                    "placeholder": "e.g. Management & Strategy / Software Engineering",
                    "maxlength": 100,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Describe what you learn and study in this course...",
                    "rows": 3,
                }
            ),
            "credits": NumberInput(
                attrs={
                    "min": 1,
                    "max": 12,
                    "placeholder": "3",
                }
            ),
            "journal": Textarea(
                attrs={
                    "placeholder": "Weekly reflections, artifacts, or project summaries...",
                    "rows": 4,
                }
            ),
        }
