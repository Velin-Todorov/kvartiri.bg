# Generated by Django 4.2.1 on 2023-07-30 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_views', '0034_remove_landlordprofile_offerings_and_more'),
        ('home_view', '0003_delete_landlord_delete_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Property',
        ),
        migrations.DeleteModel(
            name='Town',
        ),
    ]
