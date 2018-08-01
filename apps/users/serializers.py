from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserProfileSerializer(serializers.ModelSerializer):

    followers = serializers.SlugRelatedField(
        many=True,
        slug_field='email',
        read_only=True
    )
    following = serializers.SlugRelatedField(
        many=True,
        slug_field='email',
        read_only=True
    )

    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'email',
            'name',
            'job',
            'followers',
            'following',
        )
