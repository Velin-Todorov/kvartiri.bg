# Generated by Django 4.2.1 on 2023-07-30 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth_views', '0034_remove_landlordprofile_offerings_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('STUDIO', 'Studio'), ('APPARTMENT', 'Appartment'), ('SINGLE_ROOM', 'Single Room')], default='ROOM', max_length=15)),
                ('price_per_month', models.DecimalField(decimal_places=2, max_digits=20)),
                ('size', models.IntegerField()),
                ('town', models.CharField(blank=True, max_length=15)),
                ('address', models.TextField()),
                ('furnished', models.BooleanField()),
                ('utilities_included', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('landlord', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_views.landlordprofile')),
            ],
        ),
    ]