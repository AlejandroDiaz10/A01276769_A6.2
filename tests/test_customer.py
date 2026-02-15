"""Unit tests for Customer class."""

import unittest
import os
import json
from src.customer import Customer


class TestCustomer(unittest.TestCase):
    """Test cases for Customer class."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.test_data_file = "data/customers.json"
        # Clean up before each test
        if os.path.exists(self.test_data_file):
            os.remove(self.test_data_file)

    def tearDown(self):
        """Clean up after each test method."""
        if os.path.exists(self.test_data_file):
            os.remove(self.test_data_file)

    def test_create_customer_success(self):
        """Test creating a customer successfully."""
        customer = Customer("C001", "John Doe", "john@email.com", "1234567890")
        result = customer.create_customer()
        self.assertTrue(result)

        # Verify customer was saved
        customers = Customer.load_customers()
        self.assertIn("C001", customers)
        self.assertEqual(customers["C001"]["name"], "John Doe")

    def test_create_customer_duplicate(self):
        """Test creating a duplicate customer (negative case)."""
        customer1 = Customer("C001", "John Doe", "john@email.com", "1234567890")
        customer1.create_customer()

        # Try to create duplicate
        customer2 = Customer("C001", "Jane Doe", "jane@email.com", "0987654321")
        result = customer2.create_customer()
        self.assertFalse(result)

    def test_delete_customer_success(self):
        """Test deleting an existing customer."""
        customer = Customer("C001", "John Doe", "john@email.com", "1234567890")
        customer.create_customer()

        result = Customer.delete_customer("C001")
        self.assertTrue(result)

        # Verify customer was deleted
        customers = Customer.load_customers()
        self.assertNotIn("C001", customers)

    def test_delete_customer_not_found(self):
        """Test deleting a non-existent customer (negative case)."""
        result = Customer.delete_customer("C999")
        self.assertFalse(result)

    def test_display_customer_success(self):
        """Test displaying an existing customer."""
        customer = Customer("C001", "John Doe", "john@email.com", "1234567890")
        customer.create_customer()

        result = Customer.display_customer("C001")
        self.assertIsNotNone(result)
        self.assertEqual(result["customer_id"], "C001")
        self.assertEqual(result["name"], "John Doe")

    def test_display_customer_not_found(self):
        """Test displaying a non-existent customer (negative case)."""
        result = Customer.display_customer("C999")
        self.assertIsNone(result)

    def test_modify_customer_success(self):
        """Test modifying customer information."""
        customer = Customer("C001", "John Doe", "john@email.com", "1234567890")
        customer.create_customer()

        result = Customer.modify_customer(
            "C001", name="John Smith", email="johnsmith@email.com"
        )
        self.assertTrue(result)

        # Verify modifications
        customers = Customer.load_customers()
        self.assertEqual(customers["C001"]["name"], "John Smith")
        self.assertEqual(customers["C001"]["email"], "johnsmith@email.com")

    def test_modify_customer_not_found(self):
        """Test modifying a non-existent customer (negative case)."""
        result = Customer.modify_customer("C999", name="Ghost User")
        self.assertFalse(result)

    def test_load_customers_file_not_exists(self):
        """Test loading customers when file doesn't exist."""
        customers = Customer.load_customers()
        self.assertEqual(customers, {})

    def test_load_customers_invalid_json(self):
        """Test loading customers with invalid JSON (negative case)."""
        os.makedirs("data", exist_ok=True)
        with open(self.test_data_file, "w", encoding="utf-8") as f:
            f.write("invalid json content {{{")

        customers = Customer.load_customers()
        self.assertEqual(customers, {})


if __name__ == "__main__":
    unittest.main()
