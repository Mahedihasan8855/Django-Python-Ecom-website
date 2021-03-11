from django.contrib import admin
from Order.models import Shop_Cart,ShoppingCartForm,OrderProduct,Order

# Register your models here.
class Shop_CartAdmin(admin.ModelAdmin):
    list_display = ['product', 'user','quantity', 'price', 'amount',]
    list_filter = ['user',]

class OrderProductline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('user', 'product', 'price', 'quantity', 'amount')
    can_delete = False
    extra = 0
    

class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name','phone', 'total', 'status', 'transaction_id', ]
    list_filter = ['status',]
    readonly_fields=('user','first_name', 'last_name','phone', 'address', 'city', 'country', 'total','ip','transaction_id')
    can_delete = False
    inlines = [OrderProductline]
    
class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'price', 'quantity', 'amount']
    list_filter = ['user']

admin.site.register(Shop_Cart,Shop_CartAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderProduct,OrderProductAdmin)


