"""Customer module for hotel reservation system."""

import json
import os


class Customer:
    """Represents a customer in the hotel reservation system."""

    DATA_FILE = "data/customers.json"

    def __init__(self, customer_id, name, email, phone):
        """
        Initialize a Customer object.

        Args:
            customer_id (str): Unique identifier for the customer
            name (str): Customer's full name
            email (str): Customer's email address
            phone (str): Customer's phone number
        """
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone

    def to_dict(self):
        """
        Convert customer object to dictionary.

        Returns:
            dict: Customer data as dictionary
        """
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
        }

    @staticmethod
    def load_customers():
        """
        Load all customers from JSON file.

        Returns:
            dict: Dictionary of customers with customer_id as key
        """
        if not os.path.exists(Customer.DATA_FILE):
            return {}

        try:
            with open(Customer.DATA_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON in {Customer.DATA_FILE}")
            return {}
        except (IOError, OSError) as e:
            print(f"Error loading customers: {e}")
            return {}

    @staticmethod
    def save_customers(customers):
        """
        Save all customers to JSON file.

        Args:
            customers (dict): Dictionary of customers to save
        """
        directory = os.path.dirname(Customer.DATA_FILE)
        if directory:  # Only create directory if path includes one
            os.makedirs(directory, exist_ok=True)
        try:
            with open(Customer.DATA_FILE, "w", encoding="utf-8") as file:
                json.dump(customers, file, indent=4, ensure_ascii=False)
        except (IOError, OSError) as e:
            print(f"Error saving customers: {e}")

    def create_customer(self):
        """
        Create a new customer and save to file.

        Returns:
            bool: True if customer created successfully, False otherwise
        """
        customers = Customer.load_customers()

        if self.customer_id in customers:
            print(f"Error: Customer {self.customer_id} already exists")
            return False

        customers[self.customer_id] = self.to_dict()
        Customer.save_customers(customers)
        print(f"Customer {self.customer_id} created successfully")
        return True

    @staticmethod
    def delete_customer(customer_id):
        """
        Delete a customer from the system.

        Args:
            customer_id (str): ID of customer to delete

        Returns:
            bool: True if deleted successfully, False otherwise
        """
        customers = Customer.load_customers()

        if customer_id not in customers:
            print(f"Error: Customer {customer_id} not found")
            return False

        del customers[customer_id]
        Customer.save_customers(customers)
        print(f"Customer {customer_id} deleted successfully")
        return True

    @staticmethod
    def display_customer(customer_id):
        """
        Display customer information.

        Args:
            customer_id (str): ID of customer to display

        Returns:
            dict: Customer data if found, None otherwise
        """
        customers = Customer.load_customers()

        if customer_id not in customers:
            print(f"Error: Customer {customer_id} not found")
            return None

        customer = customers[customer_id]
        print(f"\n{'='*50}")
        print(f"Customer ID: {customer['customer_id']}")
        print(f"Name: {customer['name']}")
        print(f"Email: {customer['email']}")
        print(f"Phone: {customer['phone']}")
        print(f"{'='*50}\n")
        return customer

    @staticmethod
    def modify_customer(customer_id, name=None, email=None, phone=None):
        """
        Modify customer information.

        Args:
            customer_id (str): ID of customer to modify
            name (str, optional): New name
            email (str, optional): New email
            phone (str, optional): New phone

        Returns:
            bool: True if modified successfully, False otherwise
        """
        customers = Customer.load_customers()

        if customer_id not in customers:
            print(f"Error: Customer {customer_id} not found")
            return False

        if name:
            customers[customer_id]["name"] = name
        if email:
            customers[customer_id]["email"] = email
        if phone:
            customers[customer_id]["phone"] = phone

        Customer.save_customers(customers)
        print(f"Customer {customer_id} modified successfully")
        return True
