from resources import app
from ...userInput import createMultipleName as gmn
from ...classes import knight


def create_a_knight():

    # validates name being by user for new knight creation
    knights_name = gmn.createMultipleName()

    # create a new knight instance of knight class
    knight.Knight(knights_name)
