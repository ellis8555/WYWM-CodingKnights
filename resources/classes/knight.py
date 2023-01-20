from abc import ABC, abstractmethod
from datetime import datetime


class Knight(ABC):
    """
    abstract knight class
    """

    #####################
    # class fields
    #####################

    # master list of knights names. This list will include duplicates
    list_of_knights_names = []

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
        # assign knights creation time
        self.__creation_time = datetime.now()
        # get class of self
        self.__knights_class = self.__class__
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

    # used to get age of knight
    def get_creation_time(self):
        return self.__creation_time

    # knights formatted birth datetime
    def get_birthday(self):
        birthdate_formatted = self.__creation_time.strftime("%A, %B %d, %Y at %I:%M %p")
        return birthdate_formatted

    # get age of knight in readable format
    def get_age(self):
        # get date instance
        current_time = datetime.now()

        # get time stamps from date instance
        current_ts = datetime.timestamp(current_time)
        birth_ts = datetime.timestamp(self.get_creation_time())

        # get a duration that can be converted in units of time
        age = round(current_ts - birth_ts)

        # format age's duration into readable time units and display to user
        if age < 60:
            if age == 1:
                return f"{self.get_name()} is {age} second old!"
            else:
                return f"{self.get_name()} is {age} seconds old!"
        elif age < 3600:
            get_minutes = round(age / 60)
            minutes_string = ""
            if get_minutes > 1:
                minutes_string = "minutes"
            else:
                minutes_string = "minute"
            get_seconds = round(age % 60)
            print(get_seconds)
            seconds_string = ""
            if get_seconds > 1:
                seconds_string = "seconds"
            else:
                seconds_string = "second"
            return f"{self.get_name()} is {get_minutes} {minutes_string} and {get_seconds} {seconds_string} old!"
        else:
            return "did you really have this program running over an hour? Nice!"

    #####################
    # setters
    #####################

    def set_name(self, new_name):
        self.__name = new_name

    #####################
    # utilities
    #####################

    @property
    @abstractmethod
    def get_class_type(self):
        pass

    @property
    @abstractmethod
    def get_formatted_type(self):
        pass

    @abstractmethod
    def __str__(self):
        pass
