# Generated by Django 4.2.1 on 2023-07-22 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_view', '0002_property_delete_room'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Landlord',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
