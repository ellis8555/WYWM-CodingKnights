from resources.validations import numeric_without_zero_range


def update_from_multiple_objects(items_list, objects_container, displayed_messages: dict, knights_new_name: str):
    """
    method that helps in updating an objects name. when users input request results in
    a result that returns duplicates this method narrows down the duplicates into a single
    object in which the name can be updated
    """
    # create a dict that will hold knights id to list number for
    # the user to select
    users_created_selection_options = {}

    # get count of object to see if user selected a name
    # that returns multiple results
    selected_objects_count = len(items_list)

    #############
    # MESSAGE_1
    #############
    print("-" * displayed_messages["number_of_dashes_message_1"] + displayed_messages["MESSAGE_1"] + "-" * displayed_messages["number_of_dashes_message_1"])
    #############
    # MESSAGE_2
    #############
    print(displayed_messages["MESSAGE_2"])

    # int for displaying knights objects
    count = 1
    # display list
    for items_object in items_list:
        selected_knight_name = items_object.get_name()
        items_id = items_object.get_id()
        users_created_selection_options[str(count)] = items_id
        print(f"{count}. name: {selected_knight_name} - id: {items_id}")
        count += 1

    # get users selection from displayed list
    user_selection = input("\nEnter your selection number..")

    # validate user can only select from displayed option numbers
    isValid = numeric_without_zero_range(user_selection, selected_objects_count)

    while not isValid:
        # display invalid entry message
        print("It seems your selection is a displayed option. Try again.")

        # get users selection from displayed list
        user_selection = input("\nEnter your selection number..")

        # validate user can only select from displayed option numbers
        isValid = numeric_without_zero_range(user_selection, selected_objects_count)

    # get the objects id that is to be deleted
    objects_id = users_created_selection_options[user_selection]

    # get the object
    this_object = objects_container[objects_id]

    # get knights previous name and return to be used in message to the user
    previous_name = this_object.get_name()

    # set knights new name
    this_object.set_name(knights_new_name)

    return previous_name
