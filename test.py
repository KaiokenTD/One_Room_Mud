# player ID function
player_ids = {}
id_range = range(1001)
player_name = "Titus"


def generate_id():
    if player_ids == {}:
        player_ids[player_name] = 1
    else:
        # convert current player_id keys into a list, index last value and increment it by 1
        # this increment creates a new player id ready to be assigned
        sorted(player_ids)
        dict_list = list(player_ids.keys())
        new_id = dict_list[-1] + 1
        

def assign_id():
    pass


def store_pid():
    pass
