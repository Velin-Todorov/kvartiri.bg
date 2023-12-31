# Generated by Django 4.2.1 on 2023-07-24 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_views', '0009_remove_userprofile_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='is_premium',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
