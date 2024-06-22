from django.contrib import admin

from .models import Transaction


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount_formatted', 'timestamp', 'origin', 'destination', 'tags')
    list_filter = ('origin', 'destination', 'timestamp')
    search_fields = ('title', 'description', 'tags')
    # prepopulated_fields = {'tags': ('title',)}

    @admin.display(description='Amount')
    def amount_formatted(self, obj):
        return f"{obj.amount:.2f}"  # Format amount with 2 decimal places

    # amount_formatted.short_description = 'Amount'
    # list_display = list_display + (amount_formatted,)  # Add formatted amount to list_display

    # def tags_list(self, obj):
    #     return obj.tags.split(',')  # Split comma-separated tags into a list

    # tags_list.short_description = 'Tags'
    # list_display = list_display + (tags_list,)  # Add list of tags to list_display

admin.site.register(Transaction, TransactionAdmin)
