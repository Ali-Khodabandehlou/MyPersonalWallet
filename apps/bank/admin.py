from django.contrib import admin

from .models import Bank, Card


class BankAdmin(admin.ModelAdmin):
    list_display = ('title', 'website')
    list_filter = ('title', )
    search_fields = ('title', )

class CardAdmin(admin.ModelAdmin):
    list_display = ('card_number', 'owner', 'bank', 'expiry_date', 'balance_formatted')
    list_filter = ('owner', 'bank', 'expiry_date')
    search_fields = ('owner', 'bank', 'expiry_date')
    # prepopulated_fields = {'tags': ('title',)}

    @admin.display(description='Balance')
    def balance_formatted(self, obj):
        return f"{obj.balance:.2f}"  # Format balance with 2 decimal places

admin.site.register(Bank, BankAdmin)
admin.site.register(Card, CardAdmin)
