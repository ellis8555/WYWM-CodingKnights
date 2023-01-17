from resources.classes import knight


def displayKnights():
    for _knight in knight.Knight.dict_of_knight_objects.values():
        print(_knight)
