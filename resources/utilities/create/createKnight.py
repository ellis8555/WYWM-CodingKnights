from ...classes import python_knight
from ...userInput import createMultipleName as gmn


def create_a_knight():

    # validates name being by user for new knight creation
    knights_name = gmn.createMultipleName()

    # create a new knight instance of knight class
    # knight.Knight(knights_name)
    python_knight.PythonKnight(knights_name)
