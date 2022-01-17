from django.contrib import admin
from burger.models import Burger


class BurgerAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    
admin.site.register(Burger, BurgerAdmin)