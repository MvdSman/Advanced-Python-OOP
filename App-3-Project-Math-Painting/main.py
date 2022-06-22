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

    # Generate canvas
    canvas.generate("files/")


main()
