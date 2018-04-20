from django.contrib import admin
from main.models import *
# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    readonly_fields = ("reg_date",)
admin.site.register(Patient,PatientAdmin)
admin.site.register(Visit)
admin.site.register(Billable)