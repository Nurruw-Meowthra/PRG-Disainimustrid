from Shape import shape

class Square(shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def __str__(self):
        return f"Size: {self.side}"