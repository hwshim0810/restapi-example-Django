from django.urls import path

from rest_auth.registration import views as registration_views
from rest_auth import views as auth_views

urlpatterns = [

    # Login
    path('login', auth_views.LoginView.as_view(), name='login'),

    # Registration
    path('', registration_views.RegisterView.as_view(), name='registration'),
]
