#!/usr/bin/env python3
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for shapes.
    """

    @abstractmethod
    def area(self):
        """
        Abstract method to return the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to return the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Circle shape.
    """

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle shape.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of a shape.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
