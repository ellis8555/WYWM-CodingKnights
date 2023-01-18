def searchForDuplicates(user_input, list_to_search):

    # get how many times user input appears in the list
    countReturned = list_to_search.count(user_input)

    # return bool. if > 1 then true
    if countReturned > 1:
        return True
    else:
        return False

