"""Reservation module for hotel reservation system."""

import json
import os


class Reservation:
    """Represents a reservation in the hotel reservation system."""

    DATA_FILE = "data/reservations.json"

    def __init__(self, reservation_id, customer_id, hotel_id):
        """
        Initialize a Reservation object.

        Args:
            reservation_id (str): Unique identifier for the reservation
            customer_id (str): ID of the customer making the reservation
            hotel_id (str): ID of the hotel being reserved
        """
        self.reservation_id = reservation_id
        self.customer_id = customer_id
        self.hotel_id = hotel_id

    def to_dict(self):
        """
        Convert reservation object to dictionary.

        Returns:
            dict: Reservation data as dictionary
        """
        return {
            "reservation_id": self.reservation_id,
            "customer_id": self.customer_id,
            "hotel_id": self.hotel_id,
        }

    @staticmethod
    def load_reservations():
        """
        Load all reservations from JSON file.

        Returns:
            dict: Dictionary of reservations with reservation_id as key
        """
        if not os.path.exists(Reservation.DATA_FILE):
            return {}

        try:
            with open(Reservation.DATA_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON in {Reservation.DATA_FILE}")
            return {}
        except (IOError, OSError) as e:
            print(f"Error loading reservations: {e}")
            return {}

    @staticmethod
    def save_reservations(reservations):
        """
        Save all reservations to JSON file.

        Args:
            reservations (dict): Dictionary of reservations to save
        """
        directory = os.path.dirname(Reservation.DATA_FILE)
        if directory:
            os.makedirs(directory, exist_ok=True)
        try:
            with open(Reservation.DATA_FILE, "w", encoding="utf-8") as file:
                json.dump(reservations, file, indent=4, ensure_ascii=False)
        except (IOError, OSError) as e:
            print(f"Error saving reservations: {e}")

    def create_reservation(self):
        """
        Create a new reservation and save to file.

        Returns:
            bool: True if reservation created successfully, False otherwise
        """
        reservations = Reservation.load_reservations()

        if self.reservation_id in reservations:
            print(f"Error: Reservation {self.reservation_id} already exists")
            return False

        reservations[self.reservation_id] = self.to_dict()
        Reservation.save_reservations(reservations)
        print(f"Reservation {self.reservation_id} created successfully")
        return True

    @staticmethod
    def cancel_reservation(reservation_id):
        """
        Cancel a reservation.

        Args:
            reservation_id (str): ID of reservation to cancel

        Returns:
            bool: True if cancelled successfully, False otherwise
        """
        reservations = Reservation.load_reservations()

        if reservation_id not in reservations:
            print(f"Error: Reservation {reservation_id} not found")
            return False

        del reservations[reservation_id]
        Reservation.save_reservations(reservations)
        print(f"Reservation {reservation_id} cancelled successfully")
        return True


if __name__ == "__main__":
    pass
