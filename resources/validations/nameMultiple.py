import re
from resources.userInput.nameInput import nameInput


def nameMultiple():
    '''
    method that accepts at most one of [.-], max of three spaces, allowing a name such as "Jean-Claude Van Damme" or "Dr. Ho"
    '''
    # name = str(input("Enter a name: "))
    name = nameInput()
    searchPattern = "^[a-zA-Z]+[\.-]?[\s]?[a-zA-Z-]*[\.-]?[\s]?[a-zA-Z]*[\.-]?[\s]?[a-zA-Z]*$"
    pattern = re.compile(searchPattern)
    isValidName = bool(re.search(pattern, name))
    if isValidName:
        print(name)
    else:
        print("Only use letters, a dot, hyphen and keep it real!")
        nameMultiple()
