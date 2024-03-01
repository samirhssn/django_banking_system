from django.contrib import admin
from transactions.models import Transaction

class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'last_name', 'account', 'amount', 
        'balance_after_transaction', 'transaction_type', 'timestamp'
    )

    def first_name(self, obj):
        return obj.first_name

    def last_name(self, obj):
        return obj.last_name

# Register the admin class with the associated model
admin.site.register(Transaction, TransactionAdmin)
