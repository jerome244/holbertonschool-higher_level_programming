#!/usr/bin/python3
"""
This module defines the Square class with custom __str__.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.

    Instantiation with size validated as a positive integer.
    """
    def __init__(self, size):
        """
        Initializes a square with given size.

        Args:
            size: size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Returns the area of the square.
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Returns a string representation of the square.
        """
        return f"[Square] {self.__size}/{self.__size}"
