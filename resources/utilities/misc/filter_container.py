def filter_container(search_item: str, container: dict):
    """
    method that filters out knights not matching users input and returns a list of matching
    names that the user input
    """
    # initialize a list that matching knight objects will be appended to
    holding_container = []

    # filter through knights objects and find matching objects with name match
    # from users input choice
    for item_id, items_object in container.items():
        item_name = items_object.get_name()
        if item_name == search_item:
            holding_container.append(items_object)

    return holding_container
