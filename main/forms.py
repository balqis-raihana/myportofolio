from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm, TextInput, Textarea, Select, URLInput, NumberInput, PasswordInput
from django.utils.html import strip_tags
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

    def clean_title(self):
        title = strip_tags(self.cleaned_data.get("title", "")).strip()
        if not title:
            raise ValidationError("Judul pengalaman tidak boleh hanya berisi tag HTML.")
        return title

    def clean_company(self):
        return strip_tags(self.cleaned_data.get("company", "")).strip()

    def clean_description(self):
        return strip_tags(self.cleaned_data.get("description", "")).strip()


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

    def clean_name(self):
        name = strip_tags(self.cleaned_data.get("name", "")).strip()
        if not name:
            raise ValidationError("Nama mata kuliah tidak boleh hanya berisi tag HTML.")
        return name

    def clean_category(self):
        category = strip_tags(self.cleaned_data.get("category", "")).strip()
        if not category:
            raise ValidationError("Kategori tidak boleh hanya berisi tag HTML.")
        return category

    def clean_description(self):
        description = strip_tags(self.cleaned_data.get("description", "")).strip()
        if not description:
            raise ValidationError("Deskripsi tidak boleh hanya berisi tag HTML.")
        return description

    def clean_journal(self):
        journal = self.cleaned_data.get("journal")
        if journal:
            return strip_tags(journal).strip()
        return journal
