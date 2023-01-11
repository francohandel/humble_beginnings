from django.shortcuts import render,redirect
from .models import User_Details,Admin_Details,Users_Bookings, Bus_details
from django.db.models import Sum,Max
from django.contrib import messages
from django.contrib.sessions.models import Session

def home(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'home.html', {})



def Admin_login(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        password = request.POST['password']
        
        if Admin_Details.objects.filter(Username=Username, Password=password).exists():
                user = Admin_Details.objects.get(Username=Username, Password=password)
                request.session['type_id'] = 'Admin'
                request.session['login'] = 'Yes'
                return redirect('/AddBusDetails/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('/Admin_login/')
    else:
        return render(request, 'Admin_login.html', {})



def User_login(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        password = request.POST['password']
        
        if User_Details.objects.filter(Username=Username, Password=password).exists():
                user = User_Details.objects.get(Username=Username, Password=password)
                request.session['u_id'] = str(user.id)
                request.session['type_id'] = 'User'
                request.session['login'] = 'Yes'
                return redirect('/MyDetails/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('/User_login/')

    else:
        return render(request, 'User_login.html', {})



def Register(request):
    if request.method == 'POST':           
        First_name = request.POST['First_name']
        Last_name = request.POST['Last_name']
        Username = request.POST['Username']
        Dob = request.POST['Dob']
        Gender = request.POST['Gender']
        Phone = request.POST['Phone']
        Email = request.POST['Email']
        Password = request.POST['Password']
        Address1 = request.POST['Address1']
        Address2 = request.POST['Address2']
        City = request.POST['City']
        final_address = Address1+ " " + Address2
        register = User_Details( First_name=First_name, Last_name=Last_name, Dob=Dob, Gender=Gender ,Phone= Phone,Email= Email,Username= Username,Password=Password,Address=final_address,City=City)
        register.save()
        messages.info(request,'User Register Successfully')
        return redirect('/User_login/')
    else:
        return render(request, 'Register.html', {})



def ViewBookings(request):
    if request.method == 'POST':           
       pass
    else:
        Uid = request.session['u_id']
        UsersBookings = Users_Bookings.objects.all().filter(Userid=Uid)
        return render(request, 'View_Bookings.html', {'UsersBookings':UsersBookings})


def Bookticket(request):
    if request.method == 'POST':
        FromCity = request.POST['fromcity']
        ToCity = request.POST['tocity']
        date = request.POST['Date']
        print(date)
        Busdetails = Bus_details.objects.all().filter(From_place=FromCity,To_place=ToCity)
        return render(request, 'Confirmseat.html', {'Busdetails':Busdetails,'Tdate':date})
    else:
        fromcity = Bus_details.objects.order_by().values('From_place').distinct()
        tocity = Bus_details.objects.order_by().values('To_place').distinct()
        return render(request, 'Bookticket.html', {'fromcity':fromcity, 'tocity':tocity})



def viewseat(request,id, date):
    Tdate = date
    bid = id
    Busd = Bus_details.objects.all().filter(B_id=bid)    
    booked = Users_Bookings.objects.all().filter(busid=bid,Travellingdate=date).exclude(status='Cancelled',)
    s = ""
    for t in booked:
        s += t.Seatnumbers + ","
    print(s)
    booked = s[:-1]
    return render(request, 'Confirmseat.html', {'Busd':Busd,'Tdate':Tdate,'booked':booked})
    




def MyDetails(request):
    if request.method == 'POST':           
       pass
    else:
        Tid = request.session['u_id']
        Userdetails = User_Details.objects.all().filter(id=Tid)
        return render(request, 'MyDetails.html', {'userdetails':Userdetails})


def AddBusDetails(request):
    if request.method == 'POST':
        bid = list(Bus_details.objects.aggregate(Max('B_id')).values())[0] or 0
        finalbid = int(bid)+1
        bid = finalbid
        FromCity = request.POST['From_City']
        ToCity = request.POST['To_City']
        date = request.POST['Date']
        ArrivingTime = request.POST['Arriving_Time']
        DepartureTime = request.POST['Departure_Time']
        Fare = request.POST['Fare']
        bustype = request.POST['bustype']
        addBus = Bus_details( B_id=bid, From_place=FromCity, To_place=ToCity,Travellingdate=date, arrival_time=ArrivingTime ,departure_time= DepartureTime,fare= Fare,typeofbus= bustype)
        addBus.save()
        messages.info(request,'Bus Details Added Successfully')
        return redirect('/ViewBusDetails/')
    else:
        return render(request, 'AddBusDetails.html', {})


def ViewBusDetails(request):
    if request.method == 'POST':           
       pass
    else:
        busdetails = Bus_details.objects.all()
        return render(request, 'ViewBusDetails.html', {'busdetails':busdetails})


def ViewUserBookings(request):
    if request.method == 'POST':           
       pass
    else:
        UsersBookings = Users_Bookings.objects.all()
        return render(request, 'ViewUserBookings.html', {'UsersBookings':UsersBookings})


def logout(request):
    Session.objects.all().delete()
    messages.info(request,'Account logout')
    return redirect('/')

   

def Confirmseat(request):
    if request.method == 'POST':
        tid = list(Users_Bookings.objects.aggregate(Max('T_id')).values())[0] or 0
        finaltid = int(tid)+1
        tid = finaltid           
        Userid = request.session['u_id']
        From_place = request.POST['From']
        To_place = request.POST['To']
        Travellingdate = request.POST['Date']
        busid = request.POST['BusId']
        fare = request.POST['Fare']
        typeofbus = request.POST['Type']
        numberOfperson = request.POST['numofperson']
        Seatnumbers = request.POST['seatnumbers']
        seats = Seatnumbers[:-1]
        total = request.POST['totalprice']
        addBus = Users_Bookings( T_id=tid, Userid=Userid, From_place=From_place, To_place=To_place ,Travellingdate= Travellingdate,busid= busid,fare= fare,numberOfperson=numberOfperson, typeofbus=typeofbus, Seatnumbers=seats, total=total, status="Notpaid")
        addBus.save()  
        request.session['tid'] = str(tid)  
        messages.info(request,'Booking Confirmed')    
        
        return redirect('/Bookticket/')
        

    else:
        return render(request, 'Confirmseat.html', {})


def ConfirmPayment(request):
    if request.method == 'POST':
        tid = request.session['tid']
        Users_Bookings.objects.filter(T_id=tid).update(status='Paid')
        del request.session['tid']
        return redirect('/Bookticket/')

    else:
        tid = request.session['tid']
        UsersBookings = Users_Bookings.objects.all().filter(T_id=tid)
        return render(request, 'ConfirmPayment.html',  {'UsersBookings':UsersBookings})


def UpdateBus(request,id):
    if request.method == 'POST':
        bid = request.POST['busid']
        FromCity = request.POST['From_City']
        ToCity = request.POST['To_City']
        date = request.POST['Date']
        ArrivingTime = request.POST['Arriving_Time']
        DepartureTime = request.POST['Departure_Time']
        Fare = request.POST['Fare']
        bustype = request.POST['bustype']
        Bus_details.objects.filter(B_id=bid).update(From_place=FromCity, To_place=ToCity,Travellingdate=date,arrival_time=ArrivingTime ,departure_time= DepartureTime,fare= Fare,typeofbus= bustype)
        messages.info(request,'Bus Details Updated')
        return redirect('/ViewBusDetails/',{})
    else:
        busdetails = Bus_details.objects.get(B_id=id)
        return render(request, 'UpdateBusDetails.html', {'busdetails':busdetails})


def DeleteBus(request,id):
    Bus_details.objects.filter(B_id=id).delete()
    messages.info(request,'Bus Details Deleted')
    return redirect('/ViewBusDetails/',{})


def CancelTicket(request,id):
    Users_Bookings.objects.filter(T_id=id).update(status='Cancelled')
    return redirect('/ViewBookings/')
    
   