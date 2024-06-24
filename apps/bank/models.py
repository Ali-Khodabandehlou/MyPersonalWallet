from django.db import models

from ..wallet.models import Owner
from ..utils.models import Base


# class Bank(Base):
#     """Bank model"""

#     title = models.CharField(max_length=20)


class Card(Base):
    """Card model"""

    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name="cards")
    # bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name="cards")
    bank = models.CharField(max_length=50)

    title = models.CharField(max_length=20, null=True, blank=True)

    card_number = models.CharField(max_length=16, unique=True)
    cvv2 = models.IntegerField(null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        if self.title is None:
            return f'{self.bank} ({self.owner})'
        return self.title
    
    @property
    def balance(self) -> float:
        # TODO: complete this method
        return 0.0
