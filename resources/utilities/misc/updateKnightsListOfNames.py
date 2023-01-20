from resources.classes.knight import Knight


def update_knights_list_of_names(previous_name: str, new_name: str):
    """
    method that removes and appends a knights name that has been changed
    """

    # get the list holding names
    knights_list = Knight.list_of_knights_names

    # remove at most one of the previous names from the list
    knights_list.remove(previous_name)

    # append the new name to the list
    knights_list.append(new_name)