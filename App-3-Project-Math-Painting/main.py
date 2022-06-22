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
    canvas_c = input("Color of canvas (either 'black' or 'white'): ")

    # Create canvas
    canvas = Canvas(canvas_w, canvas_h, canvas_c)

    # Get user inputs and keep drawing until the user wants to quit
    user_quit = False
    while not user_quit:
        shape_type = input("Shape to be drawn (either 'rectangle' or 'square'). Use '[q]uit' to stop: ").lower()
        if shape_type == "quit" or shape_type == "q":
            user_quit = True
        else:
            shape_r = int(input("Red-value of the shape: "))
            shape_g = int(input("Green-value of the shape: "))
            shape_b = int(input("Blue-value of the shape: "))
            shape_x = int(input("X-coordinate of its origin: "))
            shape_y = int(input("Y-coordinate of its origin: "))
            if shape_type == "rectangle":
                shape_w = int(input(f"Width of {shape_type}: "))
                shape_h = int(input(f"Height of {shape_type}: "))
                shape = Rectangle(shape_x, shape_y, shape_w, shape_h, (shape_r, shape_g, shape_b))
                shape.draw(canvas)
            elif shape_type == "square":
                shape_side = int(input(f"Side of {shape_type}: "))
                shape = Square(shape_x, shape_y, shape_side, (shape_r, shape_g, shape_b))
                shape.draw(canvas)
            else:
                print("Invalid input!")

    # Generate canvas
    canvas.generate("files/")


main()
