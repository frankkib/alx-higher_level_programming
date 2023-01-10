#!/usr/bin/python3
number = 00
for number in range(100):
    if number == 99:
        print("{}".format(number))
        continue
    print("{:02}".format(number), end=', ')
