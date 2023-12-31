# Generated by Django 4.2.1 on 2023-07-22 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_views', '0003_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.TextField(unique=True),
        ),
    ]
