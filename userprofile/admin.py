from django.contrib import admin
from .models import *

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'phone', 'email', 'pix']
    
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'phone', 'price', 'qty', 'amount', 'paid']

class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'first_name', 'last_name', 'phone', 'amount', 'paid']

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Payment, PaymentAdmin)

