"""APS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from app import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.SignupPage, name='signup'),
    path('login/', views.LoginPage, name='login'),
    path('home/', views.HomePage, name='home'),
    path('logout/', views.LogoutPage, name='logout'),
    path('get-started/', views.getstarted, name='get-started'),
    path('bookappointment/', views.bookappointment, name='bookappointment'),
    path('payment/', views.paymentpage, name='payment'),
    path('signs/', views.signspage, name='signs'),
    path('Sagittarius/', views.Sagittariuspage, name='Sagittarius'),
    path('capricon/', views.capriconpage, name='capricon'),
    path('Aquarius/', views.Aquariuspage, name='Aquarius'),
    path('Aries/', views.Ariespage, name='Aries'),
    path('Libra/', views.Librapage, name='Libra'),
    path('Gemini/', views.Geminipage, name='Gemini'),
    path('Leo/', views.Leopage, name='Leo'),
    path('Scorpio/', views.Scorpiopage, name='Scorpio'),
    path('Virgo/', views.Virgopage, name='Virgo'),
    path('Taurus/', views.Tauruspage, name='Taurus'),
    path('Pisces/', views.Piscespage, name='Pisces'),
    path('Cancer/', views.Cancerpage, name='Cancer'),

]
