from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3



class Product:

    def __init__(self, name, color, size):

        self.name = name
        self.color = color
        self.size = size

class ProductFilter:

    @staticmethod
    def filter_by_color(products, color):

        return [p for p in products if p.color == color]

    @staticmethod
    def filter_by_size(products, size):

        return [p for p in products if p.size == size]

    @staticmethod
    def filter_by_size_and_color(products, color, size):

        return [p for p in products if p.color == color and p.size == size]
    


products = [
   Product("Apple", Color.GREEN, Size.SMALL),
   Product("Tree", Color.GREEN, Size.LARGE),
   Product("House", Color.BLUE, Size.LARGE)
]

pf = ProductFilter()

print("Green products:")
for p in pf.filter_by_color(products, Color.GREEN):
    print(p.name)

print("Large blue products:")
for p in pf.filter_by_size_and_color(products, Size.LARGE, Color.BLUE):
    print(p.name)