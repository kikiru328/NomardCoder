from django.db import models


# Create your models here.
class CommonModel(models.Model):
    """Common Model Definition"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class meta:
        abstract = True  # 데이터베이스에 기록되지 않을 것임을 의미.
        # CommonModel 자체 table을 기록하지 않는다.
