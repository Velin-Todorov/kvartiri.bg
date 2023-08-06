# Generated by Django 4.2.1 on 2023-08-06 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_views', '0045_remove_landlordprofile_properties_and_more'),
        ('properties', '0009_alter_property_liked_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='furnished',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No')], default='YES', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='liked_by',
            field=models.ManyToManyField(to='auth_views.profile'),
        ),
        migrations.AlterField(
            model_name='property',
            name='utilities_included',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No')], default='YES', max_length=3, null=True),
        ),
    ]
