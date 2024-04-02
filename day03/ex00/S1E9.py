from abc import ABC, abstractmethod


class Character(ABC):
    """Your docstring for Class"""
    @abstractmethod
    def __init__(self, first: str, is_alive: bool = True):
        pass

    @abstractmethod
    def die(self):
        pass


class Stark(Character):
    """Your docstring for Class"""
    def __init__(self, first: str, is_alive: bool = True):
        self.first = first
        self.is_alive = is_alive

    def die(self):
        self.is_alive = False
