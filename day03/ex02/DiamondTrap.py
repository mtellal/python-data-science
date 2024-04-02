from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """King class"""

    def __init__(self, first: str, is_alive: bool = True):
        Lannister.__init__(self, first, is_alive)
        super().__init__(first, is_alive)

    def die(self):
        pass

    def set_eyes(self, color: str):
        self.eyes = color

    def set_hairs(self, color: str):
        self.hairs = color

    def get_eyes(self):
        return self.eyes
    
    def get_hairs(self):
        return self.hairs


Joffrey = King("Joffrey")
print(Joffrey.__dict__)
Joffrey.set_eyes("blue")
Joffrey.set_hairs("light")
print(Joffrey.get_eyes())
print(Joffrey.get_hairs())
print(Joffrey.__dict__)

