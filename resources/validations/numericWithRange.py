# string, integer
def numeric_with_range(user_input, max_number):
    if user_input.isnumeric():
        entry = int(user_input)
        if entry > max_number:
            return False
        if entry == 0:
            return False
        else:
            return True
    else:
        return False
