# Generated by Django 4.2.1 on 2023-08-12 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_views', '0048_alter_landlordprofile_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landlordprofile',
            name='profile_picture',
            field=models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics/'),
        ),
    ]
