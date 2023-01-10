#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    list = dir(hidden_4)
    for j in range(len(list)):
        if(list[j][0] != '_' and list[j][1] != '_'):
            print('{}'.format(list[j]))
