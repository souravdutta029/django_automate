from django.contrib import admin
from .models import Student, Customer, Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'employee_name', 'designation', 'salary', 'retirement', 'other_benefits', 'total_benefits', 'total_compensation')

admin.site.register(Student)
admin.site.register(Customer)
admin.site.register(Employee, EmployeeAdmin)