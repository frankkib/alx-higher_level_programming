#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    result = 0
    for num in range(list_length):
        try:
            result = my_list_1[num] / my_list_2[num]
        except (ZeroDivisionError):
            print("division by 0")
            continue
        except (IndexError):
            print("out of range")
            continue
        except (TypeError):
            print("wrong type")
        finally:
            new_list.append(result)
            return (new_list)
