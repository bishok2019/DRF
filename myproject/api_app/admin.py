from django.contrib import admin

# Register your models here.
from .models import Student
# Register your models here.
admin.site.register(Student)
# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name', 'roll', 'city']