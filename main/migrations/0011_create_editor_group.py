from django.db import migrations


def create_editor_group(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    Permission = apps.get_model("auth", "Permission")
    ContentType = apps.get_model("contenttypes", "ContentType")

    editor_group, _ = Group.objects.get_or_create(name="Editor")

    # Grant change permissions for Experience and Coursework
    models_to_permit = ["experience", "coursework"]
    for model_name in models_to_permit:
        try:
            content_type = ContentType.objects.get(app_label="main", model=model_name)
            change_perm = Permission.objects.filter(
                content_type=content_type,
                codename=f"change_{model_name}"
            ).first()
            if change_perm:
                editor_group.permissions.add(change_perm)
        except Exception:
            pass


def remove_editor_group(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    Group.objects.filter(name="Editor").delete()


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0010_experience_starred_by"),
        ("auth", "0012_alter_user_first_name_max_length"),
        ("contenttypes", "0002_remove_content_type_name"),
    ]

    operations = [
        migrations.RunPython(create_editor_group, reverse_code=remove_editor_group),
    ]
