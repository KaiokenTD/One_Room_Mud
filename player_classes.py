class Player:

    def __init__(self, player_name, hp, max_hp, player_id, room_id, dead=False):
        self._player_name = player_name
        self._hp = hp
        self._max_hp = max_hp
        self._player_id = player_id
        self._room_id = room_id
        self._dead = dead

    def stats(self):
        pass
