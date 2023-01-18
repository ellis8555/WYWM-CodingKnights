def numeric_without_zero_range(user_input, max_number):
    if user_input.isnumeric():
        entry = int(user_input)
        if entry == 0:
            return False
        if entry > max_number:
            return False
        else:
            return True
    else:
        return False