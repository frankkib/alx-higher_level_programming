#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    for num in range(x):

        try:
            print("{}".format(my_list[num]), end='')
            counter += 1
        except indexError:
            break
        else:
            print()
            return (counter)

        if _name_ == "_main_":
            safe_print_list(my_list, x)
