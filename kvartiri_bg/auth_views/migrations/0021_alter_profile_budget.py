# Generated by Django 4.2.1 on 2023-07-25 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_views', '0020_alter_profile_budget'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='budget',
            field=models.CharField(choices=[(None, 'Other'), ('0-500', '0-500'), ('500-1000', '500-1000'), ('1000+', '1000+')], max_length=15, null=True),
        ),
    ]
