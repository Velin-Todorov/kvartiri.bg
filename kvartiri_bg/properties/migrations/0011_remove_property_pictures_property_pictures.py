# Generated by Django 4.2.1 on 2023-08-06 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0010_alter_property_furnished_alter_property_liked_by_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='pictures',
        ),
        migrations.AddField(
            model_name='property',
            name='pictures',
            field=models.ManyToManyField(to='properties.picture'),
        ),
    ]
