from django.contrib import admin

from app.models import Customer

admin.site.site_title ="Nakuru Sacco Customers"
admin.site.site_header = "Mars Application"
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name','email','gender']
    list_per_page = 20
    search_fields = ['name','email','dob','phone']
    list_filter = ['gender']
admin.site.register(Customer,CustomerAdmin)