# Generated by Django 4.2.1 on 2023-08-10 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_views', '0048_alter_landlordprofile_location_and_more'),
        ('properties', '0025_alter_property_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='favourite',
            field=models.ManyToManyField(blank=True, default=None, related_name='favourite', to='auth_views.profile'),
        ),
    ]