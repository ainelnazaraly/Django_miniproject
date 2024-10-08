# Generated by Django 5.1.1 on 2024-10-08 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_comment_created_at_post_created_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="content",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="post",
            name="title",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
