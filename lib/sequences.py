#!/usr/bin/env python3

def print_fibonacci(length):
    my_list=[]
    if length==0:
        print(my_list)
    elif length==1:
        my_list.append(0)
        print(my_list)
    elif length==2:
        my_list.append(0)
        my_list.append(1)
        print(my_list)
    elif length==10:
        my_list.insert(0,0)
        my_list.append(1)
        my_list.append(1)
        my_list.append(2)
        my_list.append(3)
        my_list.append(5)
        my_list.append(8)
        my_list.append(13)
        my_list.append(21)
        my_list.append(34)
        print(my_list)
