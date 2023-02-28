the_arena = {
    "The Arena": {
        "The arena floor is soaked in blood.": ["None"]
    }
}


class Room:
    """
    Root room object
    """
    def __init__(self, room_name, description, exits, room_id):
        self._room_name = room_name
        self._description = description
        self._exits = exits
        self._room_id = room_id
