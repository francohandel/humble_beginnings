from django.db import models

class Admin_Details(models.Model):
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'Admin_Details' 


class User_Details(models.Model):
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Dob = models.CharField(max_length=50,default=None)
    Gender = models.CharField(max_length=10)
    Phone = models.IntegerField(default=None)
    Email = models.EmailField()
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'User_Details'


class Users_Bookings(models.Model):
    T_id = models.IntegerField(default=None)
    Userid = models.IntegerField(default=None)
    Room_no = models.CharField(max_length=100)
    Bookingdate = models.DateField() 
    roomid = models.IntegerField(default=None)
    fare = models.IntegerField(default=None)
    numberOfperson = models.IntegerField(default=None)
    Seatnumbers = models.CharField(max_length=100,default=None)
    total = models.IntegerField(default=None)
    status = models.CharField(max_length=100,default=None)
    
    class Meta:
        db_table = 'Users_Bookings'


class room_details(models.Model):
    B_id = models.IntegerField(default=None)
    Room_no = models.CharField(max_length=100)
    Bookingdate = models.DateField()
    fare = models.CharField(max_length=100)
    
    
    class Meta:
        db_table = 'room_details'