from django.contrib import admin

from inflows import models


class InflowAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'product', 'quantity', 'created_at', 'updated_at',)
    search_fields = ('supplier__name', 'product__title',)


admin.site.register(models.Inflow, InflowAdmin)
