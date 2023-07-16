"""hack URL Configuration

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
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.login,name='login'),
   path("",views.home,name='home'),
   path('login/register',views.register,name='register'),
   path('login/login',views.login,name='login'),
   path('logout/',views.logout,name='logout'),
    path('video/',views.video,name='video'),
    path('yogaguru/',views.yogaguru,name='yogaguru'),
    path('solution/',views.solution,name='solution'),
     path('yogaguru/yogaguru',views.solution,name='solution'),
      path('about/',views.about,name='about'),
      path('contact/',views.contact,name='contact'),
      path('yogaguru/titliasana',views.knee,name='titliasana'),
      path('yogaguru/padmasana',views.padmasana,name='padmasana'),
]
