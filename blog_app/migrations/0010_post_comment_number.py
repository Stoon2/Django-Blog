# Generated by Django 4.0.3 on 2022-03-23 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0009_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comment_number',
            field=models.IntegerField(default=0),
        ),
    ]
