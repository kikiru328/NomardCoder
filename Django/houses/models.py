from django.db import models

# Create your models here.


class House(models.Model):
    """Model Definition for Houses"""

    def __str__(self):
        return self.name

    # describe data
    name = models.CharField(max_length=140)  # house 이름
    price_per_night = models.PositiveIntegerField(
        verbose_name="Price", help_text="Postive Numbers Only"
    )  # 양수
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(
        default=True,
        help_text="Does this house allow pets?",
        verbose_name="Pets Allowed?",
    )
