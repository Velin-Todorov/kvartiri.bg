# Generated by Django 4.2.1 on 2023-08-06 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_views', '0044_alter_landlordprofile_properties_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='landlordprofile',
            name='properties',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='favourites',
        ),
    ]
