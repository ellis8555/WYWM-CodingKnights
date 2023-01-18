from resources.classes.knight import Knight


def get_single_name_exists(data_to_check: str, get_data_container: dict):
    knight: Knight

    for item_id, value in get_data_container.items():
        if value == data_to_check.get_name():
            knight = value

    return knight

