"""Hotel module for hotel reservation system."""

import json
import os


class Hotel:
    """Represents a hotel in the reservation system."""

    DATA_FILE = "data/hotels.json"

    def __init__(self, hotel_id, name, location, total_rooms):
        """
        Initialize a Hotel object.

        Args:
            hotel_id (str): Unique identifier for the hotel
            name (str): Hotel's name
            location (str): Hotel's location
            total_rooms (int): Total number of rooms in the hotel
        """
        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.total_rooms = total_rooms
        self.available_rooms = total_rooms
        self.reservations = []

    def to_dict(self):
        """
        Convert hotel object to dictionary.

        Returns:
            dict: Hotel data as dictionary
        """
        return {
            "hotel_id": self.hotel_id,
            "name": self.name,
            "location": self.location,
            "total_rooms": self.total_rooms,
            "available_rooms": self.available_rooms,
            "reservations": self.reservations,
        }

    @staticmethod
    def load_hotels():
        """
        Load all hotels from JSON file.

        Returns:
            dict: Dictionary of hotels with hotel_id as key
        """
        if not os.path.exists(Hotel.DATA_FILE):
            return {}

        try:
            with open(Hotel.DATA_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON in {Hotel.DATA_FILE}")
            return {}
        except (IOError, OSError) as e:
            print(f"Error loading hotels: {e}")
            return {}

    @staticmethod
    def save_hotels(hotels):
        """
        Save all hotels to JSON file.

        Args:
            hotels (dict): Dictionary of hotels to save
        """
        directory = os.path.dirname(Hotel.DATA_FILE)
        if directory:
            os.makedirs(directory, exist_ok=True)
        try:
            with open(Hotel.DATA_FILE, "w", encoding="utf-8") as file:
                json.dump(hotels, file, indent=4, ensure_ascii=False)
        except (IOError, OSError) as e:
            print(f"Error saving hotels: {e}")

    def create_hotel(self):
        """
        Create a new hotel and save to file.

        Returns:
            bool: True if hotel created successfully, False otherwise
        """
        hotels = Hotel.load_hotels()

        if self.hotel_id in hotels:
            print(f"Error: Hotel {self.hotel_id} already exists")
            return False

        hotels[self.hotel_id] = self.to_dict()
        Hotel.save_hotels(hotels)
        print(f"Hotel {self.hotel_id} created successfully")
        return True

    @staticmethod
    def delete_hotel(hotel_id):
        """
        Delete a hotel from the system.

        Args:
            hotel_id (str): ID of hotel to delete

        Returns:
            bool: True if deleted successfully, False otherwise
        """
        hotels = Hotel.load_hotels()

        if hotel_id not in hotels:
            print(f"Error: Hotel {hotel_id} not found")
            return False

        del hotels[hotel_id]
        Hotel.save_hotels(hotels)
        print(f"Hotel {hotel_id} deleted successfully")
        return True

    @staticmethod
    def display_hotel(hotel_id):
        """
        Display hotel information.

        Args:
            hotel_id (str): ID of hotel to display

        Returns:
            dict: Hotel data if found, None otherwise
        """
        hotels = Hotel.load_hotels()

        if hotel_id not in hotels:
            print(f"Error: Hotel {hotel_id} not found")
            return None

        hotel = hotels[hotel_id]
        print(f"\n{'='*50}")
        print(f"Hotel ID: {hotel['hotel_id']}")
        print(f"Name: {hotel['name']}")
        print(f"Location: {hotel['location']}")
        print(f"Total Rooms: {hotel['total_rooms']}")
        print(f"Available Rooms: {hotel['available_rooms']}")
        print(f"Reservations: {len(hotel['reservations'])}")
        print(f"{'='*50}\n")
        return hotel

    @staticmethod
    def modify_hotel(hotel_id, name=None, location=None):
        """
        Modify hotel information.

        Args:
            hotel_id (str): ID of hotel to modify
            name (str, optional): New name
            location (str, optional): New location

        Returns:
            bool: True if modified successfully, False otherwise
        """
        hotels = Hotel.load_hotels()

        if hotel_id not in hotels:
            print(f"Error: Hotel {hotel_id} not found")
            return False

        if name:
            hotels[hotel_id]["name"] = name
        if location:
            hotels[hotel_id]["location"] = location

        Hotel.save_hotels(hotels)
        print(f"Hotel {hotel_id} modified successfully")
        return True

    @staticmethod
    def reserve_room(hotel_id, reservation_id):
        """
        Reserve a room in the hotel.

        Args:
            hotel_id (str): ID of hotel
            reservation_id (str): ID of reservation

        Returns:
            bool: True if reserved successfully, False otherwise
        """
        hotels = Hotel.load_hotels()

        if hotel_id not in hotels:
            print(f"Error: Hotel {hotel_id} not found")
            return False

        if hotels[hotel_id]["available_rooms"] <= 0:
            print(f"Error: No available rooms in hotel {hotel_id}")
            return False

        hotels[hotel_id]["available_rooms"] -= 1
        hotels[hotel_id]["reservations"].append(reservation_id)
        Hotel.save_hotels(hotels)
        print(f"Room reserved in hotel {hotel_id}")
        return True

    @staticmethod
    def cancel_reservation(hotel_id, reservation_id):
        """
        Cancel a reservation in the hotel.

        Args:
            hotel_id (str): ID of hotel
            reservation_id (str): ID of reservation to cancel

        Returns:
            bool: True if cancelled successfully, False otherwise
        """
        hotels = Hotel.load_hotels()

        if hotel_id not in hotels:
            print(f"Error: Hotel {hotel_id} not found")
            return False

        if reservation_id not in hotels[hotel_id]["reservations"]:
            print(f"Error: Reservation {reservation_id} not found in hotel")
            return False

        hotels[hotel_id]["available_rooms"] += 1
        hotels[hotel_id]["reservations"].remove(reservation_id)
        Hotel.save_hotels(hotels)
        print(f"Reservation {reservation_id} cancelled in hotel {hotel_id}")
        return True
