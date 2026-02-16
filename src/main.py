"""Main program for Hotel Reservation System."""

import sys
import os

# Add parent directory to path to allow imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.customer import Customer
from src.hotel import Hotel
from src.reservation import Reservation


def display_menu():
    """Display main menu options."""
    print("\n" + "=" * 50)
    print("HOTEL RESERVATION SYSTEM")
    print("=" * 50)
    print("1. Customer Management")
    print("2. Hotel Management")
    print("3. Reservation Management")
    print("4. Exit")
    print("=" * 50)


def customer_menu():
    """Display and handle customer management menu."""
    while True:
        print("\n--- CUSTOMER MANAGEMENT ---")
        print("1. Create Customer")
        print("2. Display Customer")
        print("3. Modify Customer")
        print("4. Delete Customer")
        print("5. Back to Main Menu")

        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            customer_id = input("Customer ID: ").strip()
            name = input("Name: ").strip()
            email = input("Email: ").strip()
            phone = input("Phone: ").strip()

            customer = Customer(customer_id, name, email, phone)
            customer.create_customer()

        elif choice == "2":
            customer_id = input("Customer ID: ").strip()
            Customer.display_customer(customer_id)

        elif choice == "3":
            customer_id = input("Customer ID: ").strip()
            print("Leave blank to keep current value")
            name = input("New Name: ").strip() or None
            email = input("New Email: ").strip() or None
            phone = input("New Phone: ").strip() or None

            Customer.modify_customer(customer_id, name, email, phone)

        elif choice == "4":
            customer_id = input("Customer ID: ").strip()
            Customer.delete_customer(customer_id)

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please try again.")


def hotel_menu():
    """Display and handle hotel management menu."""
    while True:
        print("\n--- HOTEL MANAGEMENT ---")
        print("1. Create Hotel")
        print("2. Display Hotel")
        print("3. Modify Hotel")
        print("4. Delete Hotel")
        print("5. Back to Main Menu")

        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            hotel_id = input("Hotel ID: ").strip()
            name = input("Name: ").strip()
            location = input("Location: ").strip()
            total_rooms = input("Total Rooms: ").strip()

            try:
                total_rooms = int(total_rooms)
                hotel = Hotel(hotel_id, name, location, total_rooms)
                hotel.create_hotel()
            except ValueError:
                print("Error: Total rooms must be a number")

        elif choice == "2":
            hotel_id = input("Hotel ID: ").strip()
            Hotel.display_hotel(hotel_id)

        elif choice == "3":
            hotel_id = input("Hotel ID: ").strip()
            print("Leave blank to keep current value")
            name = input("New Name: ").strip() or None
            location = input("New Location: ").strip() or None

            Hotel.modify_hotel(hotel_id, name, location)

        elif choice == "4":
            hotel_id = input("Hotel ID: ").strip()
            Hotel.delete_hotel(hotel_id)

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please try again.")


def reservation_menu():
    """Display and handle reservation management menu."""
    while True:
        print("\n--- RESERVATION MANAGEMENT ---")
        print("1. Create Reservation")
        print("2. Cancel Reservation")
        print("3. Back to Main Menu")

        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            reservation_id = input("Reservation ID: ").strip()
            customer_id = input("Customer ID: ").strip()
            hotel_id = input("Hotel ID: ").strip()

            # Verify customer exists
            customers = Customer.load_customers()
            if customer_id not in customers:
                print(f"Error: Customer {customer_id} not found")
                continue

            # Verify hotel exists and reserve room
            if Hotel.reserve_room(hotel_id, reservation_id):
                reservation = Reservation(reservation_id, customer_id, hotel_id)
                if reservation.create_reservation():
                    print("Reservation created and room reserved successfully")
                else:
                    # Rollback hotel reservation if reservation creation fails
                    Hotel.cancel_reservation(hotel_id, reservation_id)

        elif choice == "2":
            reservation_id = input("Reservation ID: ").strip()

            # Load reservation to get hotel_id
            reservations = Reservation.load_reservations()
            if reservation_id in reservations:
                hotel_id = reservations[reservation_id]["hotel_id"]

                # Cancel reservation and free room
                if Reservation.cancel_reservation(reservation_id):
                    Hotel.cancel_reservation(hotel_id, reservation_id)
                    print("Reservation and room freed successfully")
            else:
                print(f"Error: Reservation {reservation_id} not found")

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please try again.")


def main():
    """Main program loop."""
    print("\nWelcome to the Hotel Reservation System!")

    while True:
        display_menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            customer_menu()
        elif choice == "2":
            hotel_menu()
        elif choice == "3":
            reservation_menu()
        elif choice == "4":
            print("\nThank you for using Hotel Reservation System!")
            print("Goodbye!\n")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
