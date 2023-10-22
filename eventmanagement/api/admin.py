from django.contrib import admin
from .models import College, Student, Event, CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'college', 'is_staff', 'is_superuser')

admin.site.register(College)
admin.site.register(Student)
admin.site.register(Event)