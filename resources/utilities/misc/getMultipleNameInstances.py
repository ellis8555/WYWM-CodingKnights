from resources.classes.knight import Knight


def get_multiple_name_instances(data_to_check: str, get_data_container: dict):
    """
    method that returns a list of objects that match a users requested input
    this list is for a request that returned duplicates
    this list will be shortened to a single object elsewhere
    """
    knights: list

    for item_id, value in get_data_container.items():
        if value == data_to_check.get_name():
            knights.append(value)

    return knights