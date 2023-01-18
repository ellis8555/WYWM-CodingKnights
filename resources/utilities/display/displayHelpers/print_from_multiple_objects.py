from resources.classes.knight import Knight
from resources.validations import numeric_with_range


def print_from_multiple_objects(items_list, displayed_messages: dict):

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
    isValid = numeric_with_range(user_selection, selected_objects_count)

    if isValid:

        knights_object = Knight.dict_of_knight_objects.get(items_id)
        print(knights_object)

    else:
        #############
        # MESSAGE_3
        #############
        print(displayed_messages["MESSAGE_3"])
