from django.db import models

# from ..wallet.models import Owner
from ..utils.models import Base


# class Broker(Base):
#     """Broker model"""

#     title = models.CharField(max_length=20)


# class BrokerWallet(Base):
#     """BrokerWallet model"""

#     owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name="broker_wallets")
#     Broker = models.ForeignKey(Broker, on_delete=models.CASCADE, related_name="broker_wallets")

#     title = models.CharField(max_length=20, null=True, blank=True)

#     def __str__(self) -> str:
#         if self.title is None:
#             return f'{self.bank.title} ({self.owner})'
#         return self.title
    
#     def balance(self) -> float:
#         # TODO: complete this method
#         return 0.0
