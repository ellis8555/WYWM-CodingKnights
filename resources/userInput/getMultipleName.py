import re

from ..validations import threeNames


def nameMultiple():
    """
    method that accepts at most one of [.-], max of three spaces, allowing a name such as "Jean-Claude Van Damme" or
    "Dr. Ho"
    """
    # name = str(input("Enter a name: "))
    name = str(input("Enter a name: "))
    searchPattern = threeNames
    pattern = re.compile(searchPattern)
    isValidName = bool(re.search(pattern, name))
    if isValidName:
        print(name)
    else:
        print("Three names max. Single '.' and '-' can be used as well.")
        nameMultiple()
