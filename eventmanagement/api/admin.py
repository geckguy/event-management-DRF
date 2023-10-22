from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import College, Student, Event, CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'name', 'college', 'is_staff', 'is_superuser')
    list_filter = ('email', 'name', 'college', 'is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'college')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'college', 'password1', 'password2')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(College)
admin.site.register(Student)
admin.site.register(Event)
