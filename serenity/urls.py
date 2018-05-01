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

# https://docs.djangoproject.com/en/2.0/topics/auth/default/#django.contrib.auth.views.LoginView
#   Reference to learn Django's login and logout classes
from django.contrib.auth.views import LoginView, LogoutView

# Import the functions we made in views
from .views import landing_page, signup_view

urlpatterns = [
    # Admin path
    path("admin/", admin.site.urls),

    # Includes all url's from user subapp to be after this user path
    path("user/", include('user.urls')),

    # Path for landing page when function is called in views.py
    path("", landing_page, name="landing_page"),

    # Path for login
    #   If called with a GET, a login form is displayed that
    #   POSTs to the same URL.
    #   If called with a POST with user submitted credentials, it tries to log
    #   the user in by redirecting to the LOGIN_REDIRECT_URL specified in settings.py.
    #   If login is not successful, the login form gets redisplayed.
    path("login/",
        LoginView.as_view(template_name="serenity/login-form.html"),
        name="user_login"),

    # Path for logout
    #   Uses the LOGOUT_REDIRECT_URL specified in settings.py.
    path("logout/",
        LogoutView.as_view(),
        name="user_logout"),

    # Path for signup form when function is called in views.py
    path("signup/", signup_view, name="user_signup")
]
