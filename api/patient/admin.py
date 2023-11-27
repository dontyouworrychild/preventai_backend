from django.contrib import admin

from .models import *

admin.site.register(Patient)
admin.site.register(Interview)
admin.site.register(RehabCenter)
admin.site.register(Doctor)
admin.site.register(TimeSlot)
