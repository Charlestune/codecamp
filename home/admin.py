from django.contrib import admin
from . models import CompanyProfile, Type, Phone 
from . models import Contact
# Register your models here.

class CompanyProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'logo', 'carousel1', 'carousel2', 'carousel3', 'banner', 'copyright']

class TypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'brand', 'color']
    

class PhoneAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'name', 'pix', 'slug','price', 'discount_price', 'best_selling', 'latest', 'featured', 'uploaded_at', 'uploaded_at']
    prepopulated_fields = {'slug':('name',)}

class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'sent']

admin.site.register(CompanyProfile, CompanyProfileAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Phone, PhoneAdmin)
admin.site.register(Contact, ContactAdmin)