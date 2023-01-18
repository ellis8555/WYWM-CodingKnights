def searchForDuplicates(data_to_check: str, list_to_compare: list):

    # get how many times user input appears in the list
    countReturned = list_to_compare.count(data_to_check)

    # return bool. if > 1 then true
    if countReturned > 1:
        return True
    else:
        return False

