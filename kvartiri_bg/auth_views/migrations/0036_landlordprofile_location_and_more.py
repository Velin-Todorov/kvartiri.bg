# Generated by Django 4.2.1 on 2023-07-31 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_views', '0035_remove_landlordprofile_is_verified_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='landlordprofile',
            name='location',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='landlordprofile',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='current_occupation',
            field=models.CharField(choices=[('OTHER', 'Other'), ('STUDENT', 'Student'), ('WORKER', 'Worker')], default='OTHER', max_length=15),
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='budget',
            field=models.CharField(choices=[('0 Lv. - 500 Lv.', '0 Lv. - 500 Lv.'), ('500 Lv. - 1000 Lv.', '500 Lv. - 1000 Lv.'), ('1000+ Lv.', '1000+ Lv.')], default='0 Lv. - 500 Lv.', max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='looking_for',
            field=models.CharField(choices=[('STUDIO', 'Studio'), ('APPARTMENT', 'Appartment'), ('SINGLE_ROOM', 'Single Room')], default='STUDIO', max_length=11),
        ),
    ]
