# main.py
from src.Table import Seat, Table
from src.openspace import OpenSpace

if __name__ == "__main__":
    colleague_names = ["Jean", "Julo", "Hazem", "Sahar", "Bryan", "Lea", "Omar", "Oleh"]

    open_space = OpenSpace()


    open_space.organize(colleague_names)


    open_space.display()


    print(f"Number of people in the room: {open_space.get_number_of_people()}")
    print(f"Number of available seats: {open_space.get_number_of_available_seats()}")
    print(f"Number of seats left: {open_space.get_number_of_seats_left()}")
