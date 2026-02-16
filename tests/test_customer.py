"""Unit tests for Customer class."""

import unittest
import os
from src.customer import Customer


class TestCustomer(unittest.TestCase):
    """Test cases for Customer class."""

    @classmethod
    def setUpClass(cls):
        """Set up test environment once before all tests."""
        # Save original DATA_FILE path
        cls.original_data_file = Customer.DATA_FILE
        # Use a test-specific file to avoid conflicts with real data
        Customer.DATA_FILE = "test_customers.json"

    @classmethod
    def tearDownClass(cls):
        """Clean up after all tests."""
        # Restore original DATA_FILE
        Customer.DATA_FILE = cls.original_data_file
        # Delete test file if it exists
        if os.path.exists("test_customers.json"):
            os.remove("test_customers.json")

    def setUp(self):
        """Set up test fixtures before each test method."""
        # Clean up before each test
        if os.path.exists(Customer.DATA_FILE):
            os.remove(Customer.DATA_FILE)

    def tearDown(self):
        """Clean up after each test method."""
        # Clean up after each test
        if os.path.exists(Customer.DATA_FILE):
            os.remove(Customer.DATA_FILE)

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
        # Create invalid JSON file
        with open(Customer.DATA_FILE, "w", encoding="utf-8") as f:
            f.write("invalid json content {{{")

        customers = Customer.load_customers()
        self.assertEqual(customers, {})


if __name__ == "__main__":
    unittest.main()
