from django.contrib import admin
from myapp.models import Contact
from .models import *
# Register your models here.

admin.site.register(Contact)

@admin.register(payment)
class paymentAdmin(admin.ModelAdmin):
    list_display=['name','email','screenshot']

@admin.register(cake)
class PhotosAdmin(admin.ModelAdmin):
    list_display = ['cakeid']
    list_display_links = ['cakeid']


# class cartAdmin(admin.ModelAdmin):
#     list_display = ['user','total_amt','order_dt']
# admin.site.register(cart,cartAdmin)

# class cartorderAdmin(admin.ModelAdmin):
#     list_display = ['item','image','qty','price','total']
# admin.site.register(cartorder,cartorderAdmin)

# @admin.register(usercake)
# class PhotosAdmin(admin.ModelAdmin):
#     list_display = ['cakeid']
#     list_display_links = ['cakeid']

# @admin.register(ShoppingCart)
# class ShoppingCartAdmin(admin.ModelAdmin):
#     list_display = ('user', 'get_items_display')

#     def get_items_display(self, obj):
#         return ", ".join([item.name for item in obj.items.all()])

#     get_items_display.short_description = 'Items in Cart'

#     list_filter = ('user',)


@admin.register(usercake)
class usercakeAdmin(admin.ModelAdmin):
    list_display = ('c','u','status')