from django.urls import path
from django.urls import include

from rest_auth.registration import views as registration_views
from rest_auth import views as auth_views

from . import views

urlpatterns = [

    # User
    path('<int:pk>/', include([
        path(
            'follow/',
            views.FollowViewSet.as_view({
                'post': 'create',
                'get': 'list'
            }),
            name='follow'
        ),
        path('unfollow/', views.FollowViewSet.as_view({'delete': 'destroy'}), name='unfollow'),
        path('', views.UserViewSet.as_view({'get': 'retrieve'}), name='profile'),
    ])),

    path('me/', views.UserViewSet.as_view({'get': 'retrieve_me'}), name='profile'),

    # Login
    path('login/', auth_views.LoginView.as_view(), name='login'),

    # Registration
    path('/', registration_views.RegisterView.as_view(), name='registration'),

]
