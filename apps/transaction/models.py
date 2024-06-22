from django.db import models

from ..bank.models import Card
from ..broker.models import BrokerWallet
from ..utils.models import Base
from ..wallet.models import Owner


# class Transaction(Base):
#     """Transaction model"""

#     card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name="transactions", null=True, blank=True)
#     broker_wallet = models.ForeignKey(BrokerWallet, on_delete=models.CASCADE, related_name="transactions", null=True, blank=True)

#     owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name="transactions")

#     timestamp = models.DateTimeField()
#     amount = models.FloatField()

#     INCOME = "INCOME"
#     EXPENSE = "EXPENSE"
#     TYPE_CHOICES = (
#         (INCOME, INCOME),
#         (EXPENSE, EXPENSE),
#     )
#     type = models.CharField(max_length=7, choices=TYPE_CHOICES)

#     description = models.CharField(max_length=100, null=True, blank=True)

#     def __str__(self) -> str:
#         return f'{self.type}: {self.amount} at {self.timestamp}'


class Transaction(Base):
    """Transaction Model"""

    title = models.CharField(max_length=50)
    timestamp = models.DateTimeField()
    amount = models.FloatField()

    origin = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)

    description = models.TextField()
    tags = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f'{self.amount} for {self.title} on {self.timestamp}'
