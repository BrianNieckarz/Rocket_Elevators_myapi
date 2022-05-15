from django.contrib import admin
from .models import Employees, Image
# Register your models here.
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user_id')
admin.site.register(Employees, EmployeesAdmin)
admin.site.register(Image)