#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        maxi = None
        for k, v in a_dictionary.items():
            if maxi is None or a_dictionary[k] > maxi:
                maxi = a_dictionary[k]
                highest = k
        return highest
