from django.urls import path
from django.urls import include


from . import views


urlpatterns = [

    path('posts/', include([
        path(
            '<int:pk>/',
            views.PostViewSet.as_view({
                'patch': 'partial_update',
                'delete': 'destroy'
            }),
            name='post_detail'
        ),
        path(
            '',
            views.PostViewSet.as_view({
                'post': 'create',
            }),
            name='posts'
        ),
    ])),

    path('images/', include([
        path(
            '<int:pk>/',
            views.ImageViewSet.as_view({
                'patch': 'partial_update',
                'delete': 'destroy'
            }),
            name='post_detail'
        ),
        path(
            '',
            views.ImageViewSet.as_view({
                'post': 'create',
            }),
            name='images'
        )
    ])),

    path('', views.FeedViewSet.as_view({'get': 'list'}), name='feeds'),

]
