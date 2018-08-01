from rest_framework import viewsets
from rest_framework import filters
from rest_framework import status
from rest_framework.response import Response

from django.db.models import Q
from django.core.cache import cache
from django.db.utils import ProgrammingError

from feeds import models
from feeds import serializers


class FeedViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.FeedSerializer
    queryset = models.Content.objects.all()
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('-updated_at', '-created_at')

    def list(self, request, *args, **kwargs):
        feeds = cache.get('feeds')

        if not feeds:
            response = super().list(request, *args, **kwargs)
            cache.set('feeds', response.data)
            return response

        return Response(status=status.HTTP_200_OK, data=feeds)

    def get_queryset(self):
        return super().get_queryset().filter(
            Q(user__in=self.request.user.following.all()) |
            Q(user=self.request.user)
        )


class ContentViewSet(viewsets.ModelViewSet):

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.user != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)

        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_queryset(self):
        try:
            return super().get_queryset().instance_of(self.serializer_class.Meta.model)
        except ProgrammingError:
            pass


class PostViewSet(ContentViewSet):

    serializer_class = serializers.PostSerializer


class ImageViewSet(ContentViewSet):

    serializer_class = serializers.ImageSerializer
    model = models.Image

