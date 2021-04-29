class Square:
    w: float

    def __init__(self, w: float):
        self.w = w

    def area(self) -> float:
        return(self.w * self.w)

class Circle:
    r: float = 1.0

    def __init__(self, r: float):
        self.r = r

    def area(self) -> float:
        return 3.14 * (self.r * self.r)


a_circle: Circle = Circle(10.0)
a_square: Square = Square(3.0)

total: float = a_square.area()
total += a_circle.area()
print(total)
print(a_circle)