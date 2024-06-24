from django.contrib import admin

from .models import Owner


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('show_name', 'first_name', 'last_name')
    list_filter = ('first_name', 'last_name', 'nick_name')
    search_fields = ('first_name', 'last_name', 'nick_name')
    # prepopulated_fields = {'tags': ('title',)}

admin.site.register(Owner, OwnerAdmin)
