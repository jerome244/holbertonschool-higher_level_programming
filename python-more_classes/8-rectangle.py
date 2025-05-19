#!/usr/bin/python3
"""Defines a Rectangle class with width, height, area, perimeter,
string/repr representations, instance tracking, deletion message, custom print symbol support,
and comparison utilities."""

class Rectangle:
    """Represents a rectangle with private width and height attributes,
    tracks the number of instances, provides print symbol customization,
    and includes methods for comparison based on area."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle, validating attributes and updating instance count."""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle, or 0 if width or height is 0."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the rectangle drawn with the print_symbol, or an empty string if width or height is 0."""
        if self.__width == 0 or self.__height == 0:
            return ""
        row = str(self.print_symbol) * self.__width
        return "\n".join([row for _ in range(self.__height)])

    def __repr__(self):
        """Return a string representation able to recreate a new instance via eval()."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message when a Rectangle instance is deleted and decrement instance count."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with the greater or equal area.

        Args:
            rect_1 (Rectangle): First rectangle to compare.
            rect_2 (Rectangle): Second rectangle to compare.

        Returns:
            Rectangle: rect_1 if its area is >= rect_2's area, otherwise rect_2.

        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
