# Generated by Django 4.2.1 on 2023-07-28 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_views', '0031_remove_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_finished',
            field=models.BooleanField(default=False),
        ),
    ]
