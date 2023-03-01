class Room:
    """
    Root room object
    """
    def __init__(self, room_name, description, room_id, exits):
        self._room_name = room_name
        self._description = description
        self._room_id = room_id
        self._exits = exits
