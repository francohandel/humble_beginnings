# Generated by Django 2.1.5 on 2019-12-11 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Admin_Details',
            },
        ),
        migrations.CreateModel(
            name='room_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('B_id', models.IntegerField(default=None)),
                ('Room_no', models.CharField(max_length=100)),
                ('Bookingdate', models.DateField()),
                ('fare', models.CharField(max_length=100)),
                
            ],
            options={
                'db_table': 'room_details',
            },
        ),
        migrations.CreateModel(
            name='User_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=50)),
                ('Last_name', models.CharField(max_length=50)),
                ('Dob', models.CharField(default=None, max_length=50)),
                ('Gender', models.CharField(max_length=10)),
                ('Phone', models.IntegerField(default=None)),
                ('Email', models.EmailField(max_length=254)),
                ('Username', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=100)),
                ('City', models.CharField(max_length=100)),
                
            ],
            options={
                'db_table': 'User_Details',
            },
        ),
        migrations.CreateModel(
            name='Users_Bookings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('T_id', models.IntegerField(default=None)),
                ('Userid', models.IntegerField(default=None)),
                ('Room_no', models.CharField(max_length=100)),
                ('Bookingdate', models.DateField()),
                ('roomid', models.IntegerField(default=None)),
                ('fare', models.IntegerField(default=None)),
                ('numberOfperson', models.IntegerField(default=None)),
                ('Seatnumbers', models.IntegerField(default=None)),
                ('total', models.IntegerField(default=None)),
            ],
            options={
                'db_table': 'Users_Bookings',
            },
        ),
    ]
