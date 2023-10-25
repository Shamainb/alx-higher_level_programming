#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    weight = 0
    score = 0
    for row in range(len(my_list)):
        weight += my_list[row][1]
        course = 1
        for i in my_list[row]:
            course *= i
        score += course
    return (score / weight)
