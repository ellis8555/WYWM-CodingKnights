class Knight:
    """
    notes to be added
    """
#####################
# field
#####################

    __name: str

#####################
# constructor
#####################

    def __init__(self, name):
        self.__name = name

#####################
# getters
#####################

    def get_name(self):
        return self.__name

#####################
# setters
#####################

    def set_name(self, new_name):
        self.__name = new_name
