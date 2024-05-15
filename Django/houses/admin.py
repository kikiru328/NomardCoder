from django.contrib import admin
from .models import House
# Register your models here.

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    pass # 객체 상속 및 복사 (수정하지 않음)