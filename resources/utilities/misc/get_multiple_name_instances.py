from resources.classes.knight import Knight


def get_multiple_name_instances(data_to_check: str, get_data_container: dict):
    knights: list

    for item_id, value in get_data_container.items():
        if value == data_to_check.get_name():
            knights.append(value)

    return knights