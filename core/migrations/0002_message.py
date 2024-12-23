# Generated by Django 5.1.3 on 2024-11-25 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.EmailField(max_length=254)),
                ('date_sended', models.DateTimeField(auto_now_add=True)),
                ('context', models.TextField()),
            ],
        ),
    ]
