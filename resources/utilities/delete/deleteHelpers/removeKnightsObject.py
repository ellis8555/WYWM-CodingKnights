def remove_knights_object(object_to_remove, objects_container: dict):

    # get the id of the object to be removed
    object_id = object_to_remove.get_id()

    del objects_container[object_id]
