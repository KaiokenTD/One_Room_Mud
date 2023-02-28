import player_classes
import room_classes
import random
import functions
import time


# dictionaries

default_player_values = {
    "max_hp": 100,
    "level": 1,
    "location": 1,

}
# variables

dead = False


def sleep(n=1):
    time.sleep(n)


def login_screen():
    print("Welcome to One Room Mud.\n")


while not dead:
    login_screen()
    sleep()
    player_name = functions.validate_user_name()
    print("You Died.")
    dead = True
    #  print("{}, you existence awaits.".format(player_name))


