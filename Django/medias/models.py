from django.db import models
from common.models import CommonModel

# Create your models here.


class Photo(CommonModel):
    file = models.ImageField()
    description = models.CharField(
        max_length=140,
    )
    room = models.ForeignKey(
        "rooms.Room",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="Photos",
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="Photos",
    )

    def __str__(self):
        return "Photo File"


class Video(CommonModel):
    file = models.FileField()
    experience = models.OneToOneField(
        "experiences.Experience",
        on_delete=models.CASCADE,
        related_name="videos",
    )

    def __str__(self):
        return "Video File"
