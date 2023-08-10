# Generated by Django 4.2.1 on 2023-08-10 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_views', '0046_alter_landlordprofile_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landlordprofile',
            name='location',
            field=models.TextField(choices=[('SOFIA', 'Sofia'), ('PLOVDIV', 'Plovdiv'), ('VARNA', 'Varna'), ('BURGAS', 'Burgas'), ('RUSE', 'Ruse'), ('STARA ZAGORA', 'Stara Zagora'), ('PLEVEN', 'Pleven'), ('SLIVEN', 'Sliven'), ('DOBRICH', 'Dobrich'), ('SHUMEN', 'Shumen'), ('PERNIK', 'Pernik'), ('HASKOVO', 'Haskovo'), ('YAMBOL', 'Yambol'), ('Pazardzhik', 'Pazardzhik'), ('BLAGOEVGRAD', 'Blagoevgrad'), ('VELIKO TARNOVO', 'Veliko Tarnovo'), ('VIDIN', 'Vidin'), ('MONTANA', 'Montana'), ('LOVECH', 'Lovech'), ('RAZGRAD', 'Razgrad')], default='Sofia', max_length=20),
        ),
        migrations.AlterField(
            model_name='landlordprofile',
            name='type',
            field=models.CharField(choices=[('Private Owner', 'PRIVATE OWNER'), ('Company', 'COMPANY')], default='PRIVATE OWNER', max_length=15),
        ),
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('Tenant', 'TENANT'), ('Landlord', 'LANDLORD')], default='TENANT', max_length=11),
        ),
    ]