from django.contrib import admin
from employee.models import Employee
from common.models import Address, Phone


class AddressAdmin(admin.TabularInline):
    model = Address
    extra = 1

class PhoneAdmin(admin.TabularInline):
    model = Phone
    extra = 1

class EmployeeAdmin(admin.ModelAdmin):
    search_fields = ('nit', 'name', 'last_name')
    list_filter = ('gender', 'salary')
    list_display = ('name', 'last_name', 'gender', 'birthday', 'nit','salary')

    #exclude = ('last_name',)
    inlines = (AddressAdmin,PhoneAdmin)



admin.site.register(Employee,EmployeeAdmin)
# Register your models here.
