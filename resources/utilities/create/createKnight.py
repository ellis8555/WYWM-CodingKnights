from ...classes import python_knight, java_knight
from ...userInput import createMultipleName as gmn
from ...validations import numericWithoutZeroRange as nonZero


def create_a_knight():

    print("What type of knight would you like to create?\n"
          "1. Java\n"
          "2. Python\n")

    user_selection = input("Enter your choice: ")

    isValid = nonZero.numeric_without_zero_range(user_selection, 2)

    while not isValid:
        print("Enter a valid number. Try again.")
        user_selection = input("Enter your choice: ")
        isValid = nonZero.numeric_without_zero_range(user_selection, 2)

    # validates name being by user for new knight creation
    knights_name = gmn.createMultipleName()

    if user_selection == "1":

        # create a new knight instance of knight class
        java_knight.JavaKnight(knights_name)

    elif user_selection == "2":

        # create a new knight instance of knight class
        python_knight.PythonKnight(knights_name)


