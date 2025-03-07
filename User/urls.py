
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from .import views

urlpatterns = [
    path("", views.index),
    path("index.html", views.index),
    path("about.html", views.about),
    path("contact.html", views.contact),
    path("login.html", views.login),
    path("signup.html", views.signup),
    # path("signup.html", views.register),
    path("forms.html", views.forms),
    path("sell_deed.html", views.selldeed),
    path("agreement.html", views.agreement),
    path("documents.html", views.documents),
    path("registration.html", views.registration),
    path("track_application.html", views.applicationstatus),
    path("tax.html", views.tax),

    # path('login/', auth_views.LoginView.as_view(), name='login'),
    path("register", views.register, name="register"),
    path("login_user", views.login_user, name="login_user"),
    path("logout_user", views.logout_user, name="logout_user"),

    # path('application_status.html', views.check_status, name='check_status'),
]
