from django.db import migrations

def create_superuser(apps, schema_editor):
    from django.contrib.auth import get_user_model
    User = get_user_model()
    
    # Check if 'admin' already exists
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            email='balqis.ray9@gmail.com',
            password='YourStrongPassword123!'  # <-- Choose a password you will remember
        )

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_experience_company'),  # matches your previous migration
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]
