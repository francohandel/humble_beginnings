# Generated by Django 2.1.5 on 2019-12-13 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBusSeat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users_bookings',
            name='Seatnumbers',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
