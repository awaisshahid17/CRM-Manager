from django.contrib import admin
from .models import Promocode


# Register your models here.

class PromocodeAdmin(admin.ModelAdmin):
    list_display =  ["code",'is_Available','is_free','PROMO_TYPE','AMOUNT','PERCENT','amount_percent']
    search_fields =  ["code",'is_Available','is_free','PROMO_TYPE','AMOUNT','PERCENT','amount_percent']

admin.site.register(Promocode, PromocodeAdmin)
