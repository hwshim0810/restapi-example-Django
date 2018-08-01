from django.urls import path

from rest_auth.registration import views as registeration_views

urlpatterns = [

    # Registration
    path('', registeration_views.RegisterView.as_view(), name='registration'),
]
