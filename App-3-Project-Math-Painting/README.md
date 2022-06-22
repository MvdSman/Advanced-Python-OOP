# Math Painting

## Description

An app that:

* Gets as input:
  * The size of the canvas.
  * The start (origin) coordinates of geometric shapes such as squares and rectangles.
  * The dimensions and colors of these shapes.
* Returns:
  * An image with all shapes drawn onto it.

## Initial Design

### Classes, Attributes & Methods

* Square
  * Required attributes: x, y, side, color
  * Methods: draw(canvas)
* Rectangle
  * Required attributes: x, y, width, height, color
  * Methods: draw(canvas)
* Canvas
  * Required attributes: width, height, color
  * Methods: generate(imagepath)