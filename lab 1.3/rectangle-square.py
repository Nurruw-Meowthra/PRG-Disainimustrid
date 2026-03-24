class rectangle:

    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def __str__ (self):
        return f"Width: {self.width}, Height: {self.height}"
    
    def width(self):
        return self.width
    
    def height(self):
        return self.height
    
class square(rectangle):

    def __init__(self, size):
        super().__init__(size, size)

    def sides(self):
        return self.width, self.height

    def area(self):
        return self.width * self.height

    def __str__ (self):
        return f"Size: {self.width}"


"""Test functions"""
if __name__ == "__main__":
    rect = rectangle(4, 6)
    print(rect)
    print(f"Area: {rect.area()}")

    sq = square(5)
    print(sq)
    print(f"Area: {sq.area()}")