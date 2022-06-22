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
        pass


class Square(Rectangle):
    """
    Object representing a colored, square geometric shape with equal sides.
    """
    # def __init__(self, x, y, side, color):
    #     self.x = x
    #     self.y = y
    #     self.width = side
    #     self.height = side
    #     self.color = color

    def draw(self, canvas):
        pass
