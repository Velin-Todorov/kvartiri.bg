# Generated by Django 4.2.1 on 2023-08-10 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0024_alter_property_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='type',
            field=models.CharField(choices=[('STUDIO', 'Studio'), ('APPARTMENT', 'Appartment'), ('SINGLE ROOM', 'Single Room')], default='ROOM', max_length=15),
        ),
    ]