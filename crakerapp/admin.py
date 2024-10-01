from django.contrib import admin
from .models import Items,Order,OrderItem

class ItemAdmin(admin.ModelAdmin):
    list_display=('item_number','item_name','price')
    list_filter=('item_number','item_name','price')

class OrderAdmin(admin.ModelAdmin):
    list_display=('order_id','customer_name','phone_number','total_amount')
    list_filter=('order_id','customer_name','phone_number','total_amount')

class OrderItemAdmin(admin.ModelAdmin):
    list_display=('order','item','quantity','item_price')
    list_filter=('order','item','quantity','item_price')

admin.site.register(Items,ItemAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem,OrderItemAdmin)
