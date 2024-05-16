from django.contrib import admin
from .models import House

# Register your models here.


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    # pass # 객체 상속 및 복사 (수정하지 않음)

    # fields = (
    #     "name",
    #     "address",
    #     ("price_per_night", "pets_allowed")
    # )
    # search_fields = ("address",)

    # list_display_links = ("name", "address")
    # list_editable = ("pets_allowed", ) # list에서 수정 가능
    # #exclude = ("price_per_night",)
    list_display = ("name", "price_per_night", "address", "pets_allowed")

    list_filter = ("price_per_night", "pets_allowed")
