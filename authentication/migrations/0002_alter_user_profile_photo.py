# Generated by Django 4.1.7 on 2023-02-23 23:32

from django.db import migrations, models
import pathlib


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_photo',
            field=models.ImageField(default=pathlib.PurePosixPath('/static/media/Portrait_placeholder.png'), null=True, upload_to=''),
        ),
    ]
