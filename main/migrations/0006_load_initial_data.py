import sys
from django.core.management import call_command
from django.db import migrations


def load_fixtures(apps, schema_editor):
    if "test" in sys.argv:
        return
    call_command("loaddata", "initial_data.json")


def reverse_fixtures(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0005_create_superuser"),
    ]

    operations = [
        migrations.RunPython(load_fixtures, reverse_code=reverse_fixtures),
    ]
