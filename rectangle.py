class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def rectangle_area(self):
        return self.length*self.width

    def rectangle_perimeter(self):
        return 2 * (self.length + self.width)

newRectangle = Rectangle(12, 10)
print(f"The area of the rectangle is {newRectangle.rectangle_area()}")
print(f"The area of the rectangle is {newRectangle.rectangle_perimeter()}")