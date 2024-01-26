# src/openspace.py
import random
import string
from src.Table import Table


class OpenSpace:
    def __init__(self, numOfTables=6):
        self.tables = [Table(random.choice(string.ascii_letters), 4) for _ in range(numOfTables)]

    def organize(self, names):
        for name in names:
            assigned = False
            while not assigned:
                random_table = random.choice(self.tables)
                if random_table.has_free_spot():
                    random_table.assign_seat(name)
                    assigned = True

    def display(self):
        for table in self.tables:
            print(table)

    def store(self, filename):
        # Implement the functionality to store the repartition in an Excel file
        pass

    def get_number_of_people(self):
        return sum(table.capacity - table.capacity_left() for table in self.tables)

    def get_number_of_available_seats(self):
        return sum(table.capacity_left() for table in self.tables)

    def get_number_of_seats_left(self):
        return sum(table.capacity_left() for table in self.tables)

    def __repr__(self):
        return repr(self.tables)
