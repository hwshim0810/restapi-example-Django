from rest_framework import serializers

from . import models


class PostSerializer(serializers.ModelSerializer):

    created_at = serializers.ReadOnlyField()
    updated_at = serializers.ReadOnlyField()

    class Meta:
        model = models.Post
        fields = (
            'title',
            'text',
            'created_at',
            'updated_at',
        )


class ImageSerializer(serializers.ModelSerializer):

    created_at = serializers.ReadOnlyField()
    updated_at = serializers.ReadOnlyField()

    class Meta:
        model = models.Image
        fields = (
            'path',
            'caption',
            'created_at',
            'updated_at',
        )


class FeedSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Content

    def to_representation(self, instance):
        if isinstance(instance, models.Post):
            return PostSerializer(instance, context=self.context).to_representation(instance)
        elif isinstance(instance, models.Image):
            return ImageSerializer(instance, context=self.context).to_representation(instance)

        return super(FeedSerializer, self).to_representation(instance)
