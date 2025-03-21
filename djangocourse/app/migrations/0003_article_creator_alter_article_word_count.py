# Generated by Django 5.1.7 on 2025-03-20 07:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_create_superuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='articles', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='word_count',
            field=models.IntegerField(blank=True, default=''),
        ),
    ]
