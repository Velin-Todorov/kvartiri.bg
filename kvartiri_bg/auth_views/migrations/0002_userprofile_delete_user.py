# Generated by Django 4.2.1 on 2023-07-22 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home_view', '0003_delete_landlord_delete_user'),
        ('auth_views', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_premium', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=False)),
                ('profile_picture', models.ImageField(blank=True, upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('saved_properties', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home_view.property')),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]