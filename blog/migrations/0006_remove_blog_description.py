# Generated by Django 5.1.3 on 2024-11-23 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blog_description_blog_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='description',
        ),
    ]