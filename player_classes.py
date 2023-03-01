class Player:
    """
    Root player object
    """

    def __init__(self, player_name, hp, max_hp, player_id, room_id, dead=False):
        self._player_name = player_name
        self._hp = hp
        self._max_hp = max_hp
        self._dead = dead


class ConnectingPlayer(Player):
    """
    Root object for player connecting to the game
    """
    def __init__(self, player_id, room_id, player_name, hp, max_hp):
        super().__init__(player_name, hp, max_hp, player_id, room_id)
        self._player_id = player_id
        self._room_id = room_id
