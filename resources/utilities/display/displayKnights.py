from resources.classes import knight
from ..create import createKnight
from resources import app
from ..misc import zeroKnightsSelected


def displayKnights():
    # get a count of how many knights have been created
    knight_count = len(knight.Knight.dict_of_knight_objects)

    # if at least one knight has been created display all knights
    if knight_count > 0:
        print("-" * 20 + "Knights created" + "-" * 20)
        display_count = 1
        for _knight in knight.Knight.dict_of_knight_objects.values():
            print(f"{display_count}: {_knight}")
            display_count += 1
        print("-" * 55)
    else:
        zeroKnightsSelected.zero_knights_created()




