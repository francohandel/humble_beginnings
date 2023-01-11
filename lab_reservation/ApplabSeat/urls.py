from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Admin_login/', views.Admin_login, name='Admin_login'),
    path('User_login/', views.User_login, name='User_login'),
    path('Register/', views.Register, name='Register'),
    path('ViewBookings/', views.ViewBookings, name='ViewBookings'), 
    path('Bookticket/', views.Bookticket, name='Bookticket'),
    path('MyDetails/', views.MyDetails, name='MyDetails'),
    path('AddRoomDetails/', views.AddRoomDetails, name='AddRoomDetails'),
    path('ViewRoomDetails/', views.ViewRoomDetails, name='ViewRoomDetails'),
    path('ViewUserBookings/', views.ViewUserBookings, name='ViewUserBookings'),
    path('Confirmseat/', views.Confirmseat, name='Confirmseat'),
    path('viewseat/<slug:id>/<slug:date>', views.viewseat, name='viewseat'),
    path('ConfirmPayment/', views.ConfirmPayment, name='ConfirmPayment'),
    path('logout/', views.logout, name='logout'),
    path('UpdateRoom/<int:id>', views.UpdateRoom, name='UpdateRoom'),
    path('DeleteRoom/<int:id>', views.DeleteRoom, name='DeleteRoom'),
    path('CancelTicket/<int:id>', views.CancelTicket, name='CancelTicket'),
]