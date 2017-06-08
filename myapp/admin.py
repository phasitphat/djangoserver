from django.contrib import admin
from myapp.models import  Cart, Customer,  ContactUs,  Order, Report, Payment, ProductInOrder, Product, Category
from .models import User

class CustomerAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Customer._meta.fields]

admin.site.register(Customer,CustomerAdmin)

class CartAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Cart._meta.fields]

admin.site.register(Cart,CartAdmin)

# class AddressAdmin(admin.ModelAdmin):
# 	list_display=[f.name for f in Address._meta.fields]

# admin.site.register(Address,AddressAdmin)

class ContactUsAdmin(admin.ModelAdmin):
	list_display=[f.name for f in ContactUs._meta.fields]

admin.site.register(ContactUs,ContactUsAdmin)

# class PhoneAdmin(admin.ModelAdmin):
# 	list_display=[f.name for f in Phone._meta.fields]

# admin.site.register(Phone,PhoneAdmin)

class OrderAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Order._meta.fields]

admin.site.register(Order,OrderAdmin)

class ReportAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Report._meta.fields]

admin.site.register(Report,ReportAdmin)

class PaymentAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Payment._meta.fields]

admin.site.register(Payment,PaymentAdmin)

class ProductInOrderAdmin(admin.ModelAdmin):
	list_display=[f.name for f in ProductInOrder._meta.fields]

admin.site.register(ProductInOrder,ProductInOrderAdmin)

class ProductAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Product._meta.fields]

admin.site.register(Product,ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Category._meta.fields]

admin.site.register(Category,CategoryAdmin)
