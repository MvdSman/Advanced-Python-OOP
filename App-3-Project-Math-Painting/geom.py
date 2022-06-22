import painter

class Rectangle:
    """
    Object representing a colored, rectangular geometric shape.
    """
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):
        print(f"Setting color to {str(self.color)} for a rectangle with:\n"
              f"\tx={self.x}\n"
              f"\ty={self.y}\n"
              f"\twidth={self.width}\n"
              f"\theight={self.height}")
        canvas.data[self.y:(self.y + self.height), self.x:(self.x + self.width)] = self.color


class Square:
    """
    Object representing a colored, square geometric shape with equal sides.
    """
    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas):
        print(f"Setting color to {str(self.color)} for a square with:\n"
              f"\tx={self.x}\n"
              f"\ty={self.y}\n"
              f"\tside={self.side}")
        canvas.data[self.y:(self.y + self.side), self.x:(self.x + self.side)] = self.color
