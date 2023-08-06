# Generated by Django 4.2.1 on 2023-08-06 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_views', '0045_remove_landlordprofile_properties_and_more'),
        ('properties', '0012_remove_property_pictures_picture_property_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='landlord',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth_views.landlordprofile'),
        ),
        migrations.RemoveField(
            model_name='property',
            name='liked_by',
        ),
        migrations.AddField(
            model_name='property',
            name='liked_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth_views.profile'),
        ),
    ]
