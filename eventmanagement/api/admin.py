from django.contrib import admin
from .models import College, Student, Event, CustomUser

admin.site.register(College)
admin.site.register(Student)
admin.site.register(Event)
admin.site.register(CustomUser)
