from geom import Rectangle, Square
from painter import Canvas


def main():
    """
    Main function that runs on execution.
    :return:
    """

    # Get user inputs
    canvas_w = int(input("Width of canvas: "))
    canvas_h = int(input("Height of canvas: "))
    canvas_c = input("Color of canvas (either 'black', or 'white', or custom RGB as 'RRR, GGG, BBB'): ")

    # Set canvas color
    if canvas_c == "white":
        canvas_c = [255, 255, 255]
    elif canvas_c == "black":
        canvas_c = [0, 0, 0]
    else:
        canvas_c = tuple(map(int, canvas_c.split(",")))

    # Create canvas
    canvas = Canvas(canvas_w, canvas_h, canvas_c)

    # Get user inputs and keep drawing until the user wants to quit
    while True:
        shape_type = input("Shape to be drawn (either 'rectangle' or 'square'). Use '[q]uit' to stop: ").lower()
        if shape_type == "quit" or shape_type == "q":
            break
        else:
            shape_rgb = tuple(map(int, input("Color of shape (RGB as 'RRR, GGG, BBB'): ").split(",")))
            shape_x = int(input("X-coordinate of its origin: "))
            shape_y = int(input("Y-coordinate of its origin: "))
            if shape_type == "rectangle":
                shape_w = int(input(f"Width of {shape_type}: "))
                shape_h = int(input(f"Height of {shape_type}: "))
                shape = Rectangle(shape_x, shape_y, shape_w, shape_h, shape_rgb)
                shape.draw(canvas)
            elif shape_type == "square":
                shape_side = int(input(f"Side of {shape_type}: "))
                shape = Square(shape_x, shape_y, shape_side, shape_rgb)
                shape.draw(canvas)
            else:
                print("Invalid input!")

    # Generate canvas
    canvas.generate("files/")


main()
