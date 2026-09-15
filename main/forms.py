from django.forms import ModelForm, TextInput, Textarea, Select, DateTimeInput, URLInput
from main.models import Experience

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "company",
            "description",
            "category",
            "thumbnail",
            "started_at",
            "ended_at",
        ]

        labels = {
            "title": "Title / Role",
            "company": "Company / Organization",
            "description": "Description",
            "category": "Category",
            "thumbnail": "Thumbnail URL (Optional)",
            "started_at": "Start Date",
            "ended_at": "End Date (Leave blank if ongoing)",
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
            "started_at": DateTimeInput(
                attrs={
                    "type": "datetime-local",
                }
            ),
            "ended_at": DateTimeInput(
                attrs={
                    "type": "datetime-local",
                }
            ),
        }
