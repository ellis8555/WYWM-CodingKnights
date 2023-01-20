def remove_knights_object(object_to_remove, objects_container: dict):
    """
    method takes in knights object and removes that object from master dictionary
    that contains all knights objects
    """

    # get the id of the object to be removed
    object_id = object_to_remove.get_id()

    del objects_container[object_id]
