"""Create a dataclass named "Product" that has the following attributes:
    product_id: int
    name: str
    price: float
    quantity: int
The class should also have a method named "total_cost" that calculates and returns the total cost of the product, 
which is the price multiplied by the quantity.
Create a list of Product objects and write a function that takes this list as input and returns the product 
with the highest total cost.
Write a program that creates a list of 5 Product objects, prints out their attributes, 
and then calls the function to find the product with the highest total cost."""

# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from dataclasses import dataclass
from typing import List

@dataclass
class Product:
    product_id: int
    name: str
    price: float
    quantity: int

    def total_cost(self) -> float:
        total_cost = self.price * self.quantity
        return total_cost


products_list = [
    Product(1, "Apple", 0.5, 5),
    Product(2, "Pear", 1.5, 3),
    Product(3, "Banana", 1.0, 7),
    Product(4, "Pineapple", 5.0, 1),
    Product(5, "Lemon", 0.7, 9),
]


def get_most_cost(product_list: List[Product]) -> str:
    name_cost = {}
    for i, product in enumerate(product_list):
        product_cost = product.total_cost()
        name = product.name
        name_cost[name] = product_cost

    most_cost = [
        name for name, cost in name_cost.items() if cost == max(name_cost.values())
    ]
    return f"{', '.join(most_cost)} costs the most"


print(get_most_cost(products_list))

# -----------------------------------------

products_list_two = [
    (1, "Apple", 0.5, 5),
    (2, "Pear", 1.5, 3),
    (3, "Banana", 1.0, 7),
    (4, "Pineapple", 5.0, 1),
    (5, "Lemon", 0.7, 9),
]


def get_most_cost_two(product_list: List[tuple]) -> str:
    name_cost = {}
    for i, product in enumerate(product_list):
        product = Product(*product)
        # print(product)
        # print(product.total_cost())
        print(
            f"{product.name} -- price = {product.price}, quantity = {product.quantity}"
        )
        name_cost[product.name] = product.total_cost()
    most_cost = [
        name for name, cost in name_cost.items() if cost == max(name_cost.values())
    ]
    return f" {', '.join(most_cost)} costs the most"


print(get_most_cost_two(products_list_two))
