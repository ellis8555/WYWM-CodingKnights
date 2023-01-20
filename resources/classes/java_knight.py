from resources.classes.knight import Knight


class JavaKnight(Knight):

    def __init__(self, name):
        super().__init__(name)
        self.type_of_knight = self.__class__
        self.formatted_type = "Java"

    def get_class_type(self):
        return self.type_of_knight

    def get_formatted_type(self):
        return self.formatted_type

    def __str__(self):
        return f"{'-' * 36}Your selected Java knight{'-' * 36}" \
               f"\nName: {self.get_name()}" \
               f"\nID: {self.get_id()}" \
               f"\nBirth time: {self.get_birthday()}" \
               f"\nAge: {self.get_age()}" \
               f"\nKnights type: {self.get_formatted_type()}" \
               f"\nKnights class: {self.get_class_type()}" \
               f"\n{'-' * 92}"