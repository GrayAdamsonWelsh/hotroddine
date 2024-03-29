"""
URL configuration for hotroddine project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from blog.views import my_blog
from menu.views import my_menu
from signup.views import my_signup
from diary.views import my_diary
from booking.views import my_booking

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', my_blog, name='blog'),
    path('menu/', my_menu, name='menu'),
    path('signup/', my_signup, name='signup'),
    path('diary/', my_diary, name='diary'),
    path('booking/', my_booking, name='booking'),
]
