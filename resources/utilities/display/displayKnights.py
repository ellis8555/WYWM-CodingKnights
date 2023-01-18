from resources.classes import knight
from ..misc import zeroKnightsSelected


def displayKnights():
    # get a count of how many knights have been created
    knight_count = len(knight.Knight.dict_of_knight_objects)

    # if at least one knight has been created display all knights
    if knight_count > 0:
        if knight_count == 1:
            print(f"{'-' * 36}Your selected knight{'-' * 36}")
            display_count = 1
            for _knight in knight.Knight.dict_of_knight_objects.values():
                print(f"{display_count}: {_knight.get_name()}")
                display_count += 1
        else:
            print(f"{'-' * 36}Your selected knights{'-' * 36}")
            display_count = 1
            for _knight in knight.Knight.dict_of_knight_objects.values():
                print(f"{display_count}: {_knight.get_name()}")
                display_count += 1
        print("-" * 92)
    else:
        zeroKnightsSelected.zero_knights_created()




