# Generated by Django 4.1.6 on 2023-02-05 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='published_at',
            field=models.DateTimeField(max_length=20),
        ),
    ]
