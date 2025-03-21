# Generated by Django 5.1.7 on 2025-03-19 16:15

from django.db import migrations
from django.utils import timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    
    def create_superuser(apps, schema_editor):
        from django.contrib.auth import get_user_model

        User = get_user_model()

        if User.objects.exists():
            return
        
        superuser = User.objects.create_superuser(
            username="example_username",
            email="example@example.com",
            password="example_password",
            last_login=timezone.now()
        )
        superuser.save()

    operations = [
        migrations.RunPython(create_superuser)
    ]
