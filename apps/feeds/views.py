from rest_framework import viewsets
from rest_framework import filters
from rest_framework import status
from rest_framework.response import Response

from feeds import models
from feeds import serializers


class FeedViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.FeedSerializer
    queryset = models.Content.objects.all()
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('-updated_at', '-created_at')

    def get_queryset(self):
        return super().get_queryset().filter(
            user__in=self.request.user.following.all()
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


class PostViewSet(ContentViewSet):

    serializer_class = serializers.PostSerializer
    queryset = models.Content.objects.instance_of(models.Post)


class ImageViewSet(ContentViewSet):

    serializer_class = serializers.ImageSerializer
    queryset = models.Content.objects.instance_of(models.Image)

