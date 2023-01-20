from resources.utilities.misc import filter_container as fc


def multiplesReturned(user_input: str, objects_container):
    """
    method that will filter matching duplicate objects into their own container
    to be processed elsewhere
    """
    # container to hold returned objects
    knights_list = fc.filter_container(user_input, objects_container)

    return knights_list
