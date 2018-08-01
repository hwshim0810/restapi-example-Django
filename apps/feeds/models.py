from django.db import models
from django.contrib.auth import get_user_model

from polymorphic.models import PolymorphicModel

from utility.models import UpdatedAtModel


class Content(PolymorphicModel, UpdatedAtModel):

    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)


class Post(Content):

    title = models.CharField(max_length=50)
    text = models.TextField(max_length=3000)


class Image(Content):

    path = models.CharField(max_length=200)
    caption = models.TextField(max_length=3000, blank=True)

