
from abc import ABC, abstractmethod, abstractstaticmethod, abstractclassmethod


bands = []

class Band():
    """
    This class defines 
    """

    instances = []
    solo_list = []
    def __init__(self, name = "", members = []):
        self.name = str(name)
        self.members = list(members)
        Band.instances.append(self)

    def __str__(self):
        return (f"This band is called {self.name} and has {len(self.members)} members.")

    def __repr__(self):
        return (f"This band is called {self.name} and has {len(self.members)} members.")
    
    @abstractmethod
    def play_solos(cls):
        def play_solo(cls):
            pass
        return cls.solo_list


    def sign_band(self):
        if self.name not in bands:
            bands.append(self.name)
        else:
            print("Band already regestered.")
    
    @classmethod
    def to_list(cls):
        return cls.instances






class Musician(Band):
    """
    This class defines 
    """

    def __init__(self, name = "", role = "", instrument = "", sounds = ""):
        self.name = str(name)
        self.role = str(role) 
        self.instrument = str(instrument)
        sounds = str(sounds)

    def __str__ (self):
        return (f"My name is {self.name} and I play {self.instrument}")

    def __repr__ (self):
        return (f"{self.role} instance. Name = {self.name}")

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        Band.solo_list.append(self.sounds)
        return self.sounds



class Guitarist(Musician):
    """
    
    """
    def __init__(self, name = ""):
        self.name = str(name)
        self.role = "Guitarist" 
        self.instrument = "guitar"
        self.sounds = "face melting guitar solo"

class Bassist(Musician):
    """
    
    """
    def __init__(self, name = ""):
        self.name = str(name)
        self.role = "Bassist" 
        self.instrument = "bass"
        self.sounds = "bom bom buh bom"


class Drummer(Musician):
    """
    
    """
    def __init__(self, name = ""):
        self.name = str(name)
        self.role = "Drummer" 
        self.instrument = "drums"
        self.sounds = "rattle boom crash"


# if __name__ == "__main__":
#     test_band = Band("test", ["a", "b", "c"])
#     print(test_band)
#     print(test_band.to_list())
#     test_band.sign_band()
#     print(bands)
#     testman = Guitarist("testman")
#     print(testman)


