
class Seat:
    def __init__(self, id: int):
        self.id = id
        self.free = True
        self.occupant = None

    def set_occupant(self, occupantName):
        self.occupant = occupantName
        self.free = False

    def remove_occupant(self):
        occupant = self.occupant
        self.occupant = None
        self.free = True
        return occupant

    def __repr__(self):
        return f'Seat(id={self.id}, free={self.free}, occupant={self.occupant})'


class Table:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.seats = [Seat(i) for i in range(capacity)]

    def displaySeats(self):
        print(self.seats)

    def __repr__(self):
        return f'Table(name={self.name}, seats={self.seats})'

    def has_free_spot(self):
        for seat in self.seats:
            if seat.free:
                return True
        return False

    def assign_seat(self, name):
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                return True  
        return False  

    def capacity_left(self):
        return sum(1 for seat in self.seats if seat.free)
