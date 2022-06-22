from PIL import Image

class Canvas:
    """
    Object where all shapes are going to be drawn onto
    """
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    def generate(self, imagepath=""):
        pass
