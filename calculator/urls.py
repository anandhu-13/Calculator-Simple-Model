"""
URL configuration for calculator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from operations.views import AdditionView,SubtractionView,MultiplicationView,LeapyearView,EmiView,IndexView,SigninView,RegistrationView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/',AdditionView.as_view(),name="addition"),
    path('sub/',SubtractionView.as_view(),name="subtraction"),
    path('mul/',MultiplicationView.as_view(),name="multiplication"),
    path('leapyear/',LeapyearView.as_view(),name="leapyear"),
    path('emi/',EmiView.as_view(),name="emi"),
    path("",IndexView.as_view(),name="index"),
    path("login/",SigninView.as_view(),name="login"),
    path("register/",RegistrationView.as_view(),name="register"),

    
]
