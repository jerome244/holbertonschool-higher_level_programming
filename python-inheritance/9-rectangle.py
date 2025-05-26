#!/usr/bin/python3
"""
This module defines the Rectangle class with area and __str__.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.

    Instantiation with width and height validated as positive integers.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangle with width and height.

        Args:
            width: width of the rectangle.
            height: height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
