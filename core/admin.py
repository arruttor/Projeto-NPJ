from django.contrib import admin
from core.models import beneficiary, cities, marital_status, status
# Register your models here.


class BeneficiaryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class CitiesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class marital_statusAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class statusAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
 
admin.site.register(beneficiary, BeneficiaryAdmin)
admin.site.register(cities, CitiesAdmin)
admin.site.register(marital_status, marital_statusAdmin)
admin.site.register(status, statusAdmin)
