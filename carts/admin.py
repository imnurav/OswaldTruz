from django.contrib import admin
from .models import Cart, CartItem
# Register your models here.


class CardAdmin(admin.ModelAdmin):
    list_display = ('card_id', 'date_added',)


class CardItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'cart', 'quantity', 'is_active')


admin.site.register(Cart, CardAdmin)
admin.site.register(CartItem, CardItemAdmin)
