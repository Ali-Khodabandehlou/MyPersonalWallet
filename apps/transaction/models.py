from django.db import models

from ..bank.models import Card
# from ..broker.models import BrokerWallet
from ..utils.models import Base
# from ..wallet.models import Owner


class Transaction(Base):
    """Transaction Model"""

    title = models.CharField(max_length=50)
    timestamp = models.DateTimeField()
    amount = models.FloatField()

    origin = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)

#     INCOME = "INCOME"
#     EXPENSE = "EXPENSE"
#     TYPE_CHOICES = (
#         (INCOME, INCOME),
#         (EXPENSE, EXPENSE),
#     )
#     type = models.CharField(max_length=7, choices=TYPE_CHOICES)

    description = models.TextField()
    tags = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f'{self.amount} for {self.title} on {self.timestamp.date().strftime()}'
