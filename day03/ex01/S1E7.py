from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first: str, is_alive: bool = True):
        self.first_name = first
        self.is_alive = is_alive
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def die(self):
        self.is_alive = False

    def __str__(self):
        return 'Vector: ' + str((self.family_name, self.eyes, self.hairs))

    def __repr__(self):
        return 'Vector: ' + str((self.family_name, self.eyes, self.hairs))


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first: str, is_alive: bool = True):
        self.first_name = first
        self.is_alive = is_alive
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'

    def die(self):
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first: str, is_alive: bool = True):
        return cls(first, is_alive)

    def __str__(self):
        return 'Vector: ' + str((self.family_name, self.eyes, self.hairs))

    def __repr__(self):
        return 'Vector: ' + str((self.family_name, self.eyes, self.hairs))
