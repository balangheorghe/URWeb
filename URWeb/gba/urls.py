"""URWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from URWeb import home
from URWeb.login import LoginView
from django.views.generic import TemplateView
from .gba import Main, Location

urls = [
    url(r'^/temp/(?P<name>\w+)', Main.as_view(), name='temp'),
    url(r'^/location', Location.as_view(), name='location')
    #    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    #    url(r'^admin',  admin.site.urls),
    #    url(r'^login',  LoginView.as_view(template_name="login.html"), name='login'),
    #    url(r'^signup', TemplateView.as_view(template_name='signup.html'), name='signup'),
    #    url(r'^myaccount', TemplateView.as_view(template_name='myaccount.html'), name='myaccount')
]
