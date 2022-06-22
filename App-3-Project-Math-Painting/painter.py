import numpy as np
from PIL import Image

class Canvas:
    """
    Object where all shapes are going to be drawn onto
    """
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

        # Create 3d np array of zeros, default black canvas
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)

        # Set canvas color to white if the default black is not wanted
        if self.color == "white":
            self.data[:] = [255, 255, 255]

        print(f"Created a canvas with:\n"
              f"\twidth={self.width}\n"
              f"\theight={self.height}\n"
              f"\tcolor={self.color}")

    def generate(self, imagepath=""):
        # Create image
        img = Image.fromarray(self.data, "RGB")

        # Path requires a trailing "/"!
        img.save(f"{imagepath}canvas.png")
        img.show()
