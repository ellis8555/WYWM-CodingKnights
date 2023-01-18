from resources.classes.knight import Knight
from resources.validations import numeric_with_range


def print_multiple_objects(items_list, displayed_messages: dict):
    # message_inputs = {
    #     # first message that will be displayed
    #     "number_of_dashes_message_1": 30,
    #     "MESSAGE_1": "Multiple knights share that name",
    #     # second message that will be displayed
    #     "MESSAGE_2": "\nSelect which knight you are referring to..\n",
    #     "number_of_dashes_message_3": 36,
    #     # third message that will be displayed
    #     "MESSAGE_3": "Your selected knight",
    #     # attributes are within MESSAGE_3
    #     # fourth message that will be displayed
    #     "MESSAGE_4": "Appie J and Caroline!",
    # }

    message_inputs = displayed_messages

    # create a dict that will hold knights id to list number for
    # the user to select
    users_created_selection_options = {}

    # get count of object to see if user selected a name
    # that returns multiple results
    selected_objects_count = len(items_list)

    #############
    # MESSAGE_1
    #############
    print("-" * message_inputs["number_of_dashes_message_1"] + message_inputs["MESSAGE_1"] + "-" * message_inputs["number_of_dashes_message_1"])
    #############
    # MESSAGE_2
    #############
    print(message_inputs["MESSAGE_2"])

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
        #############
        # MESSAGE_3
        #############
        print("-" * message_inputs["number_of_dashes_message_3"] + message_inputs["MESSAGE_3"] + "-" * message_inputs["number_of_dashes_message_3"])

        knights_object = Knight.dict_of_knight_objects.get(items_id)
        print(knights_object)

        # create dynamic number of dashes to print to end this particular display
        dashes_in_message = message_inputs["number_of_dashes_message_3"] * 2
        length_of_message = len(message_inputs["MESSAGE_3"])
        dashes_to_display = dashes_in_message + length_of_message
        # print dashes
        print("\n" + "-" * dashes_to_display + "\n")

    else:
        #############
        # MESSAGE_4
        #############
        print(message_inputs["MESSAGE_4"])
