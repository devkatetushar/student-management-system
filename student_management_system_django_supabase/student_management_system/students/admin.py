from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_id", "full_name", "email", "course", "year", "created_by", "created_at")
    list_filter = ("course", "year", "created_at")
    search_fields = ("student_id", "full_name", "email", "course")
    readonly_fields = ("created_at",)
