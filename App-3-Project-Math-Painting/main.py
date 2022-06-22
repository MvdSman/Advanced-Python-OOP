from geom import Rectangle, Square
from painter import Canvas


def main():
    """
    Main function that runs on execution.
    :return:
    """

    # Get user inputs
    canvas_w = 640
    canvas_h = 480
    canvas_c = "black"

    # Create instances
    canvas = Canvas(canvas_w, canvas_h, canvas_c)
    rect1 = Rectangle(100, 100, 100, 50, [255, 0, 0])
    rect2 = Rectangle(200, 0, 50, 200, [25, 3, 255])
    sqre1 = Square(100, 100, 25, [0, 255, 0])

    # Draw shapes
    rect1.draw(canvas)
    rect2.draw(canvas)
    sqre1.draw(canvas)

    # Generate canvas
    canvas.generate("files/")


main()
