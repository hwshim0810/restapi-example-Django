from django.contrib.auth import get_user_model

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status

from . import serializers


class FollowViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.UserProfileSerializer
    queryset = get_user_model().objects.all()

    def create(self, request, *args, **kwargs):

        follow_target = self.get_object()

        user = request.user
        user.following.add(follow_target)
        follow_target.followers.add(user)
        user.save()

        return Response(status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):

        unfollow_target = self.get_object()

        user = request.user
        user.following.remove(unfollow_target)
        unfollow_target.followers.remove(user)
        user.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def list(self, request, *args, **kwargs):
        queryset = request.user.followers.all()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )


class UserViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.UserProfileSerializer
    queryset = get_user_model().objects.all()

    @action(methods=['GET'], detail=True)
    def retrieve_me(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)
