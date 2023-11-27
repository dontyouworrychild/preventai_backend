from django.contrib import admin
from django.contrib.auth.hashers import make_password

from .models import *

class DoctorAdmin(admin.ModelAdmin):
    exclude = ('role', 'is_staff', 'is_active', 'is_admin', 'last_login', 'groups', 'is_superuser', 'user_permissions')

    def save_model(self, request, obj, form, change):
        obj.role = "doctor"
        obj.password = make_password(obj.password)
        super().save_model(request, obj, form, change)

admin.site.register(Patient)
admin.site.register(Interview)
admin.site.register(RehabCenter)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(TimeSlot)
