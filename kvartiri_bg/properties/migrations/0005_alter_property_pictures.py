# Generated by Django 4.2.1 on 2023-08-06 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0004_picture_remove_property_landlord_alter_property_town_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='pictures',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='properties.picture'),
        ),
    ]
