class Knight:
    """
    notes to be added
    """
#####################
# field
#####################

    __name: str
    __id: int

#####################
# constructor
#####################

    def __init__(self, name):
        self.__name = name
        self.__id = id(self)

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
