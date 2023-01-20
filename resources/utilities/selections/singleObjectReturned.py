from resources.utilities.misc import filterContainer as fc


def singleObjectReturned(user_input: str, storage_container):
    """
    method that returns a single object if the user searched for an object
    that had no duplicates
    """

    # temporary container to hold single object
    holding_container = fc.filter_container(user_input, storage_container)

    return holding_container[0]



