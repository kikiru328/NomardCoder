from django.db import models


# Create your models here.
class CommonModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    uploadted_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
