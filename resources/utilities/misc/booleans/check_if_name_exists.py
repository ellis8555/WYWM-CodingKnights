def check_if_name_exists(data_to_check: str, list_to_compare: list):
    # check if users choice is a name that a knight has
    does_name_exist = data_to_check in list_to_compare

    if does_name_exist:
        return True
    else:
        return False
