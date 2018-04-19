"""serenity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib.auth.views import LoginView, LogoutView

from .views import landing_page, signup_view

urlpatterns = [
    # Admin Url
    url(r'^admin/', admin.site.urls),
    # Includes all url's from user subapp?
    url(r'^user/', include('user.urls')),
    # Url for landing page
    url(r'^$', landing_page, name="landing_page"),
    # Url for login template view
    url(r'login$',
        LoginView.as_view(template_name="serenity/login-form.html"),
        name="user_login"),
    # Url for logging out
    url(r'logout$',
        LogoutView.as_view(),
        name="user_logout"),
    path("signup/", signup_view, name = "signup_view")
]
