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
    path('AddBusDetails/', views.AddBusDetails, name='AddBusDetails'),
    path('ViewBusDetails/', views.ViewBusDetails, name='ViewBusDetails'),
    path('ViewUserBookings/', views.ViewUserBookings, name='ViewUserBookings'),
    path('Confirmseat/', views.Confirmseat, name='Confirmseat'),
    path('viewseat/<slug:id>/<slug:date>', views.viewseat, name='viewseat'),
    path('ConfirmPayment/', views.ConfirmPayment, name='ConfirmPayment'),
    path('logout/', views.logout, name='logout'),
    path('UpdateBus/<int:id>', views.UpdateBus, name='UpdateBus'),
    path('DeleteBus/<int:id>', views.DeleteBus, name='DeleteBus'),
    path('CancelTicket/<int:id>', views.CancelTicket, name='CancelTicket'),
]