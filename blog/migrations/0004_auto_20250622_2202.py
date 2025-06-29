# Generated by Django 3.2.25 on 2025-06-23 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20250622_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='calificacion',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='libro',
            name='opinion_personal',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='libro',
            name='portada',
            field=models.ImageField(blank=True, null=True, upload_to='portadas/'),
        ),
    ]
