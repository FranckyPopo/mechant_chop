from django.contrib import admin

from front.models import SiteInfo

@admin.register(SiteInfo)
class SiteInfo(admin.ModelAdmin):
    list_display = ["email", "phone", "date_create", "date_update"]