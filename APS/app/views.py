from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Appointment

from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confirm password are not same")


        my_user=User.objects.create_user(uname,email,pass1)
        my_user.save()
        return redirect('login')
        return HttpResponse("User has been created successfully")


    return render (request,'signup.html')


def LoginPage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        pass1 = request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Username or password is incorrect")

    return render(request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def getstarted(request):
    return render(request, 'get-started.html')
def bookappointment(request):
    if request.method=='POST':
        fname=request.POST.get('Firstname')
        lname=request.POST.get('Lastname')
        phno=request.POST.get('Phone Number')
        email=request.POST.get('Email')
        date=request.POST.get('Book A Date')
        gender=request.POST.get('Gender')
        message = request.POST.get('Message')

        appointment = Appointment()
        appointment.first_name = fname
        appointment.last_name = lname
        appointment.phone_number = phno
        appointment.date_of_appointment = date
        appointment.gender = gender
        appointment.message = message

        appointment.save()

        return redirect('home')
    context = {}
    return render(request, 'bookappointment.html', context=context)

def paymentpage(request):
    return render(request, 'payment.html')

def signspage(request):
    return render(request,'signs.html')

def Sagittariuspage(request):
     return render(request,'Sagittarius.html')


def capriconpage(request):
    return render(request, 'capricon.html')

def Aquariuspage(request):
    return render(request,'Aquarius.html')

def Ariespage(request):
    return render(request,'Aries.html')

def Librapage(request):
    return render(request,'Libra.html')

def Geminipage(request):
    return render(request,'Gemini.html')

def Leopage(request):
    return render(request,'Leo.html')

def Ariespage(request):
    return render(request,'Aries.html')

def Scorpiopage(request):
    return render(request,'Scorpio.html')

def Virgopage(request):
    return render(request,'Virgo.html')

def Tauruspage(request):
    return render(request,'Taurus.html')

def Piscespage(request):
    return render(request,'Pisces.html')

def Cancerpage(request):
    return render(request,'Cancer.html')
