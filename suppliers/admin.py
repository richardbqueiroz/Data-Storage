from django.contrib import admin

from suppliers import models


class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ('name',)


admin.site.register(models.Supplier, SupplierAdmin)
