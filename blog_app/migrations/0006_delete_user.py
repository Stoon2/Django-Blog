# Generated by Django 4.0.3 on 2022-03-19 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0005_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
