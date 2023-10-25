#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_list = list()
    for k in a_dictionary.keys():
        keys_list.append(k)
    for i in keys_list:
        if a_dictionary[i] == value:
            del a_dictionary[i]
    return a_dictionary
