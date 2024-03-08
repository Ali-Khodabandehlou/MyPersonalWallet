from abc import ABC, abstractmethod
from datetime import datetime


class Base(ABC):
    """A base class for your application's custom classes."""

    #  @abstractmethod
    #  def method(): ...

    def __init__(self) -> None:
        pass


class Owner(Base):
    """Represents an owner of a card."""

    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        super().__init__()
    
    def title(self) -> str:
        return f'{self.last_name}, {self.first_name}'


class Bank(Base):
    """Represents a bank institution."""

    def __init__(self, title: str) -> None:
        self.title = title
        super().__init__()

    def title(self) -> str:
        return f'{self.title}'


class Card(Base):
    """Represents a credit or debit card."""

    def __init__(self, bank: Bank, card_number: str, owner: Owner, 
                 balance: int = 0, expiry_month: str = '00', expiry_day : str = '00', cvv : str = '000'
                 ) -> None:
        self.bank = bank
        self._card_number = card_number
        self.balance = balance
        self.expiry_month = expiry_month
        self.expiry_day = expiry_day
        self._cvv = cvv

        self.owner = owner
        super().__init__()
    
    def get_card_number(self) -> str:
        return f'{self._card_number}'

    def set_card_number(self, card_number: str) -> None:
        self._card_number = card_number
    
    def title(self) -> str:
        return f'{self.bank.title} ({self.owner} - {self.balance:.2f})'


class Transaction(Base):
    """Represents a financial transaction."""

    def __init__(self, card: Card, amount: float, date: datetime, type: str, description: str = None) -> None:
        self.card: Card = card
        self.amount: float = amount
        self.date: datetime = date
        self.type: str = type

        self.description: str = description

        super().__init__()

    def title(self) -> str:
        return f"{self.type} of ${self.amount} on {self.date.strftime('%Y-%m-%d')}"
