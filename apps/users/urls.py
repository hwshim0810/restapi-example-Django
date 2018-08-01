from django.urls import path

from rest_auth.registration import views as registration_views

urlpatterns = [

    # Registration
    path('', registration_views.RegisterView.as_view(), name='registration'),
]
