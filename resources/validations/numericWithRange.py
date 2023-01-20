# string, integer
def numeric_with_range(user_input, max_number):
    """
    method that validates user input to numeric only and can include a zero
    """
    if user_input.isnumeric():
        entry = int(user_input)
        if entry > max_number:
            return False
        else:
            return True
    else:
        return False
