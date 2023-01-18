from resources.classes.knight import Knight
from resources.validations import numeric_with_range


def multiplesReturned(items_returned: int, item_list: list):
    # create a dict that will hold knights id to list number for
    # the user to select

    users_created_selection_options = {}

    # print out message informing user multiple knights share entered name
    print("-" * 30 + "Multiple knights share that name" + "-" * 30)
    print("\nSelect which knight you are referring to..\n")

    # int for displaying knights objects
    count = 1
    # display list
    for knights_object in item_list:
        selected_knight_name = knights_object.get_name()
        selected_knight_id = knights_object.get_id()
        users_created_selection_options[str(count)] = selected_knight_id
        print(f"{count}. name: {selected_knight_name} - id: {selected_knight_id}")
        count += 1

    # get users selection from displayed list
    user_selection = input("\nEnter your selection number..")

    # validate user can only select from displayed option numbers
    isValid = numeric_with_range(user_selection, items_returned)

    if isValid:
        knights_id = users_created_selection_options.get(user_selection)
        knights_object = Knight.dict_of_knight_objects.get(knights_id)
        knights_name = knights_object.get_name()
        knights_id = knights_object.get_id()
        print(f"\n{'-' * 36}Your selected knight{'-' * 36}\nname: {knights_name}\nid: {knights_id}")
    else:
        print("Apple Jack and Caroline!")