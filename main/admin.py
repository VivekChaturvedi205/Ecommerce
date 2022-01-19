from django.contrib import admin
from main.models import *

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('Name','Price','Image')
     
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=('user','name','email','phone_number')

admin.site.register(Review)
admin.site.register(CheckoutDetails)
admin.site.register(Feature)
admin.site.register(Order)
admin.site.register(OrderItem)