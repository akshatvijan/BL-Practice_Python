from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Iterable

#Abstract base class for an order

class DiscountPolicy(ABC):
    @abstractmethod
    def apply_discount(self, order_total: float) -> float:
        pass
class NoDiscount(DiscountPolicy):
    def apply_discount(self, amount: float) -> float:
        return amount
class PercentageDiscount(DiscountPolicy):
    def __init__(self, percentage: float):
        if not (0 <= percentage <= 100):
            raise ValueError("Percentage must be between 0 and 100.")
        self.percentage = percentage

    def apply_discount(self, amount: float) -> float:
        return amount * (1 - self.percentage / 100)


@dataclass
class Item:
    name: str
    __price: float

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value
    def __str__(self):
        return f"Name = {self.name}, Price = {self.price}"


class Order:
    def __init__(self,discount_policy):
        self.items = []
        self.discount_policy=discount_policy

    def add_item(self, item):
        self.items.append(item)
        

    def get_total(self):
        total = 0

        for item in self.items:
            total += item.price

        return total
    def final_amount(self):
        total = self.get_total()

        return self.discount_policy.apply_discount(total)
    def __str__(self):
        return f"The final amount is {self.final_amount()}"
    def __len__(self):
        return len(self.items)
    def __getitem__(self,index):
        return self.items[index]

i1 = Item("Laptop", 1000)
i2 = Item("Mouse", 2000)
print(i1.name)
o1 = Order(PercentageDiscount(20))

o1.add_item(i1)
o1.add_item(i2)
print(o1)
print(o1.get_total())
print(o1.final_amount())
print(len(o1))
print(o1[0])
