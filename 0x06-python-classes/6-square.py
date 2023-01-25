#!/usr/bin/python3
"""class definition"""
class Square:
    "class initialization"
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

        @property
        def size(self):
            """ getting the size"""
            return self.__size
        @property
        def poistion(self):
            """for getting the position"""
            return self.__size
        @size.setter
        def size(self, value):
            """setting the size"""
            if (type(size)is not int):
                raise TypeError("size must be an integer")
            elif (value < 0):
                raise ValueError("size must be >=0")
            else:
                self.__size = value

        @position.setter

        def position(self, value, tuple):
            """setting the position"""
            if (type(value) is not tuple):
                raise TypeError("position must be a tuple of 2 positive integers")
            elif (len(value) != 2):
                raise TypeError("position must be a tuple of 2 positive integers")
            elif (type(value[0]) is not int) or (type(value[1]) is not int):
                raise TypeError("position must be a tuple of 2 positive integers")
            elif (value8[0] < 0 ) or (value[1] < 0):
                raise TypeError("position must be a tuple of 2 positive integers")
            else:
                self.__position = value
                def area(self):
                    if self.size == 0:
                        print()
                    else:
                        for num in range(self.position[1]):
                            print("")
                            for num in range(self.size):
                                print(" " * self.position[0], end="")
                                print("#" * self.size)

