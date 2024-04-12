from abc import ABC, abstractmethod
from datetime import datetime
import os
import re

from DataBase import write_to_db, read_from_db


def print_class_detail(class_name: str) -> None:
    """prints class data read from db in a table format"""
    class_data = read_from_db(class_name)

    if not class_data:
        print('No data to show.')
        return

    rows = []

    columns = [' ']
    columns_len = len(class_data[list(class_data.keys())[0]].keys())
    for key in class_data[list(class_data.keys())[0]].keys():
        columns.append(key)
    column_width = int((100 - columns_len) / columns_len)
    vertical_border = ['----']
    for _ in range(columns_len):
        vertical_border.append('-' * column_width)
    rows.append(vertical_border)
    rows.append(columns)
    rows.append(vertical_border)
    
    for key, value in class_data.items():
        new_row = [key]
        for item in value.values():
            new_row.append(item)
        rows.append(new_row)
        rows.append(vertical_border)
    
    for i in range(len(rows)):
        if i % 2 == 0:
            separator = ' '
        else:
            separator = '|'

        print(separator, end='')
        for j in range(len(rows[i])):
            if j == 0:
                print(f'{rows[i][j]:<4}', end=separator)
            else:
                print(f'{rows[i][j]:<{column_width}}', end=separator)
        print()


class Base(ABC):
    """A base class for your application's custom classes."""

    #  @abstractmethod
    #  def method(): ...

    def __init__(self) -> None:
        pass

    def title(self) -> str:
        return 'Base Class'
    
    def info(self):
        return self.title()


class Owner(Base):
    """Represents an owner of a card."""

    def __init__(self, first_name: str = '', last_name: str = '') -> None:
        self.first_name = first_name
        self.last_name = last_name
        super().__init__()
    
    def title(self) -> str:
        return f'{self.last_name}, {self.first_name}'
    
    def owner_add(self) -> str:
        """Add a new owner"""
        first_name = input('Enter owner\'s first name: ')
        last_name = input('Enter owner\'s last name: ')
        self.first_name = first_name
        self.last_name = last_name

        # write to database
        try:
            return f'seccussfuly added owner: {self.title()}' if write_to_db('Owner', self.__dict__, 'add') else 'something went wrong'
        except:
            return 'something went wrong'


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
                 balance: int = 0, expiry_month: str = '00', expiry_day : str = '00'
                 ) -> None:
        card_number_pattern = r"^[0-9]{16}$"

        self.bank = bank

        if bool(re.match(card_number_pattern, card_number)):
            self._card_number = card_number
        else:
            raise ValueError("Invalid card number format for the specified card type.")
        
        self.balance = balance

        date_pattern = r"\d{2}"
        if bool(re.match(date_pattern, expiry_month)):
            self.expiry_month = expiry_month
        else:
            raise ValueError("Invalid cvv format.")
        if bool(re.match(date_pattern, expiry_day)):
            self.expiry_day = expiry_day
        else:
            raise ValueError("Invalid cvv format.")

        self.owner = owner
        super().__init__()
    
    def get_card_number(self) -> str:
        return f'{self._card_number}'
    
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
