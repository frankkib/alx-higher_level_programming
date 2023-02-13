#!/usr/bin/python3
"""class Rectangle defination"""
from models.base import Base


class Rectangle(Base):
    """class initialization"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """class representation"""
        self.width = width
        self.height = height
        self.x = x
        self.y = x
        super().__init__(id)

    @property
    def width(self):
        """Returns the value of the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of the rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Returns the hieght"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of the rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """returns the X co-ordinates"""
        return self.__x

    @x.setter
    def x(self, value):
        """set the X co-ordinate"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Returns the Y co-ordinate"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the Y co-orditinate"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """finds the area and return area"""
        return self.__width * self.__height

    def __str__(self):
        """Return the string representation"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)

    def display(self):
        """print tha reactangle with # symbol"""
        recta = self.__y
        for num in range(self.__height):
            if recta > 0:
                while recta > 0:
                    print()
                    recta -= 1
            print(" " * self.__x + "#" * self.__width)

    def update(self, *args, **kwargs):
        """upadtes the arguments"""
        if args is None and len(args) != 0:
            args_list = ['id', 'width', 'height', 'x', 'y']
            for num in range(len(args)):
                setattr(self, args_list[num], args[num])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary"""
        return {"id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y}
