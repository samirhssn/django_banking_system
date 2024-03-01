from django.db import models
from accounts.models import UserBankAccount, User
from .constants import TRANSACTION_TYPE_CHOICES

class Transaction(models.Model):
    account = models.ForeignKey(
        UserBankAccount,
        related_name='transactions',
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    amount = models.DecimalField(
        decimal_places=2,
        max_digits=12
    )
    balance_after_transaction = models.DecimalField(
        decimal_places=2,
        max_digits=12
    )
    transaction_type = models.PositiveSmallIntegerField(
        choices=TRANSACTION_TYPE_CHOICES
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    @property
    def first_name(self):
        return self.user.first_name if self.user else ''

    @property
    def last_name(self):
        return self.user.last_name if self.user else ''

    def __str__(self):
        return f"{self.account.account_no} - {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"

    class Meta:
        ordering = ['timestamp']
