from abc import ABC, abstractmethod


class HhAbc(ABC):
    """ Абстрактный метод класса HH. """

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def load_info(self):
        pass

    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def __str__(self):
        pass
