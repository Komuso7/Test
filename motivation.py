from Const_motivation import *

def motivation(list_data):
    creativity_points = 0
    instrumental_points = 0
    social_points = 0
    independent_points = 0
    unmotivated_points = 0
    table = {1: (1, 2, 3, 4, 5),
            2: (3, 2, 5, 4, 1),
            3: (5, 1, 2, 3, 4),
            4: (1, 4, 3, 5, 2),
            5: (2, 1, 3, 5, 4),
            6: (2, 1, 3, 4, 5),
            7: (3, 2, 1, 5, 4),
            8: (4, 1, 3, 5, 2),
            9: (3, 1, 4, 2, 5),
            10: (3, 2, 4, 1, 5),
            11: (1, 2, 4, 5, 3),
            12: (2, 3, 5, 1, 4),
            13: (1, 3, 2, 4, 5),
            14: (4, 3, 2, 1, 5),
    }
    counter = 0
    for values in table.values():
        if values[int(list_data[counter])] == 1:
            creativity_points+= 1
        elif values[int(list_data[counter])] == 2:
            instrumental_points+= 1
        elif values[int(list_data[counter])] == 3:
            social_points+= 1
        elif values[int(list_data[counter])] == 4:
            independent_points+= 1
        else:
            unmotivated_points+= 1
        counter+= 1
    print("Творческий тип мотивации: ",creativity_points)
    print("Инструментальный тип мотивации: ",instrumental_points)
    print("Социальный тип мотивации: ",social_points)
    print("Независимый тип мотивации: ",independent_points)
    print("Немотивированный тип мотивации: ",unmotivated_points)
    max_point = 0
    if max_point < creativity_points:
        max_point = creativity_points
        motivation = creativity
    if max_point < instrumental_points:
        max_point = instrumental_points
        motivation = instrumental
    if max_point < social_points:
        max_point = social_points
        motivation = social
    if max_point < independent_points:
        max_point = independent_points
        motivation = independent
    if max_point < unmotivated_points:
        max_point = unmotivated_points
        motivation = unmotivated
    return motivation
