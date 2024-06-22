from django.db import models

from ..utils.models import Base


# class Owner(Base):
#     """Owner model"""

#     first_name = models.CharField(max_length=20)
#     last_name = models.CharField(max_length=20)
#     nick_name = models.CharField(max_length=20, null=True, blank=True)

#     def __str__(self) -> str:
#         if self.nick_name is None:
#             return f'{self.first_name} {self.last_name}'
#         return self.nick_name
    

# class Wallet(Base):
#     """Wallet model"""

#     owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name="wallets")

#     def balance(self) -> int:
#         # TODO: complete this method
#         return 0
