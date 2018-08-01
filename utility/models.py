from django.db import models


class CreateAtModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class UpdatedAtModel(CreateAtModel):

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
