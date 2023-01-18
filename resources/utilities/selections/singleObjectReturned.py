from resources.utilities.misc import filter_container as fc


def singleObjectReturned(user_input: str, storage_container):

    # temporary container to hold single object
    holding_container = fc.filter_container(user_input, storage_container)

    return holding_container[0]



