from resources import app
from resources.utilities.create import createKnight


def zero_knights_created():
    """
    method that informs the user zero objects exist if the user has chosen
    a choice that requires the return of at least a single object
    """
    print("There currently are no knights that have been created")

    # get if user would like to create a knight

    choice = input("Would you like to create a knight now?\n 'y' or 'n'")
    if choice == "y":
        createKnight.create_a_knight()
    else:
        print("Ok, but you have zero knights created")
