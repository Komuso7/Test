from Const_Tomas import *
def Tomas(list_data):
    table = {1: (0, 0, 0, 1, 2),
            2: (0, 2, 1, 0, 0),
            2: (1, 0, 0, 0, 2),
            4: (0, 0, 1, 0, 2),
            5: (0, 1, 0, 2, 0),
            6: (2, 0, 0, 1, 0),
            7: (0, 0, 2, 1, 0),
            8: (1, 2, 0, 0, 0),
            9: (2, 0, 0, 1, 0),
            10: (1, 0, 2, 0, 0),
            11: (0, 1, 0, 0, 2),
            12: (0, 0, 2, 1, 0),
            13: (2, 0, 1, 0, 0),
            14: (2, 1, 0, 0, 0),
            15: (0, 0, 0, 2, 1),
            16: (2, 0, 0, 0, 1),
            17: (1, 0, 0, 2, 0),
            18: (0, 0, 2, 0, 1),
            19: (0, 1, 0, 2, 0),
            20: (0, 1, 2, 0, 0),
            21: (0, 2, 0, 0, 1),
            22: (2, 0, 1, 0, 0),
            23: (0, 1, 0, 2, 0),
            24: (0, 0, 2, 0, 1),
            25: (1, 0, 0, 0, 2),
            26: (0, 2, 1, 0, 0),
            27: (0, 0, 0, 1, 2),
            28: (1, 2, 0, 0, 0),
            29: (0, 0, 1, 2, 0),
            30: (0, 2, 0, 0, 1),
    }
    counter = -1
    rivalry_point = 0
    сollaboration_point = 0
    compromise_point = 0
    avoidance_point = 0
    adaptation_point = 0
    if list_data == 0:
        return "Неверные данные"        
    for values in table.values():
        counter += 1
        if values[0] == int(list_data[counter]):
            rivalry_point += 1
            continue
        if values[1] == int(list_data[counter]):
            сollaboration_point += 1
            continue
        if values[2] == int(list_data[counter]):
            compromise_point += 1
            continue
        if values[3] == int(list_data[counter]):
            avoidance_point += 1
            continue
        if values[4] == int(list_data[counter]):
            adaptation_point += 1

    print("Соперничество: ",rivalry_point)
    print("Сотрудничество: ",сollaboration_point)
    print("Компромисс: ",compromise_point)
    print("Избегание: ",avoidance_point)
    print("Приспособление: ",adaptation_point)
    max_point = 0
    if max_point < rivalry_point:
        max_point = rivalry_point
        motivation = rivalry
    if max_point < сollaboration_point:
        max_point = сollaboration_point
        motivation = сollaboration
    if max_point < compromise_point:
        max_point = compromise_point
        motivation = compromise
    if max_point < avoidance_point:
        max_point = avoidance_point
        motivation = avoidance
    if max_point < adaptation_point:
        max_point = adaptation_point
        motivation = adaptation
    return motivation