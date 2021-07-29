class Band():
    band_list = []

    def __init__(self,name,band):
        self.name = name
        Band.band_list.append(self)
    member_array = []

    def add_member(self, name_member):
        self.name_member = name_member
    
    def play_solos(self0):
        result = ''
        for i in Band.member_array:
            result = result + f"{i.play_solos()}"
            return result

    @classmethod
    def list_of(cls):
        return cls.member_array
    
    def __repr__(self):
        return f"to show {self.name} not true"

    
    def __str__(self):
        return f"welcome in {self.name} member of {Band.member_array}"



class Musician(Band):
    pass


class Guitarist(Musician):
    pass


class Bassist(Musician):
    pass


class Drummer(Musician):
    pass

