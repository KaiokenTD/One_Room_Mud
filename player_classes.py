class Player:

    def __init__(self, hp, max_hp, player_id, location):
        self._hp = hp
        self._max_hp = max_hp
        self._player_id = player_id
        self._location = location


class Room:

    def __init__(self, name, location, description, exits):
        self._name = name
        self._location = location
        self._description = description
        self._exits = exits
