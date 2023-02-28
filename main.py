import player_classes
import room_classes
import random
import functions
import time

# DICTIONARIES

default_player_values = {
    "hp": 100,
    "max_hp": 100,
    "level": 1,
    "room_id": 1
}

player_ids = {}

# VARIABLES

id_range = range(1, 1001)
dead = False
players_connected = []
max_hp = default_player_values.get("max_hp")
starting_hp = max_hp
level = default_player_values.get("level")
starting_room = default_player_values.get("room_id")


# FUNCTIONS

def generate_id():
    # if it's the 1st player connecting
    if player_ids == {}:
        return 1
    else:
        # convert current player_id keys into a list, index last value and increment it by 1
        # this increment creates a new player id ready to be assigned

        player_id_list = sorted(list(player_ids.keys()))
        new_id = player_id_list[-1] + 1
        return new_id


def assign_id(player_name, id_value):
    player_ids[player_name] = id_value


def sleep(n=1):
    time.sleep(n)


def welcome(player_name):
    print("{}, you existence awaits.".format(player_name))


def login_screen():
    print("Welcome to One Room Mud.\n")


while not dead:
    login_screen()
    sleep()
    player_name = functions.validate_user_name().capitalize()
    welcome(player_name)
    new_player_id = generate_id()
    assign_id(player_name, new_player_id)  # assign id info to dictionary
    players_connected.append(player_name)
# need to create a room

    player_1 = player_classes.Player(player_name, starting_hp, max_hp, new_player_id, starting_room, dead=False)
    print()

    sleep()
    print("You Died.")
    dead = True

