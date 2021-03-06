"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('message/', views.message,name='message'),
    path('about',views.about,name='about'),
    path('core/', include('core.urls')),
    path('book_ex/', include('book_ex.urls')),
    path('web_scrape/', include('web_scrape.urls')),
    path('donation/', include('donation.urls')),
    path('profile',views.profile,name='profile'),
    path('logout',views.user_logout,name='user_logout'),
]
