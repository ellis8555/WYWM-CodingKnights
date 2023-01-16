from ..utilities import searchForDuplicates as search


class Knight:
    """
    notes to be added
    """

#####################
# class fields
#####################

    # master list of knights names. This list will include duplicates
    list_of_knights_names = []
    # this list will detect for duplicate names
    list_of_duplicate_names = []
    # dictionary of knight objects with knights id as the key
    dict_of_knight_objects = {}

#####################
# constructor
#####################

    def __init__(self, name):
        # assign knights name
        self.__name = name
        # assign objects id to knights id
        self.__id = id(self)
        # check if knights name already exists in list
        temp_num = search.searchForDuplicates(
            name, Knight.list_of_knights_names)
        # if knights name is in the list then this name has a duplicate
        if temp_num > 0:
            Knight.list_of_duplicate_names.append(name)
        # del the variable that was used in counting how many names there are in the list of nights
        del temp_num
        # add knights list to master list of names. This list includes duplicates
        Knight.list_of_knights_names.append(name)
        # add knights object to dictionary with the id as the key
        Knight.dict_of_knight_objects[self.__id] = self

#####################
# getters
#####################

# name of knight
    def get_name(self):
        return self.__name

# id of knight
    def get_id(self):
        return self.__id

#####################
# setters
#####################

    def set_name(self, new_name):
        self.__name = new_name

#####################
# utilities
#####################

    def __str__(self):
        return f"{self.get_name()}"
