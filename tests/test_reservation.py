"""Unit tests for Reservation class."""

import unittest
import os
from src.reservation import Reservation


class TestReservation(unittest.TestCase):
    """Test cases for Reservation class."""

    @classmethod
    def setUpClass(cls):
        """Set up test environment once before all tests."""
        # Save original DATA_FILE path
        cls.original_data_file = Reservation.DATA_FILE
        # Use a test-specific file to avoid conflicts with real data
        Reservation.DATA_FILE = "test_reservations.json"

    @classmethod
    def tearDownClass(cls):
        """Clean up after all tests."""
        # Restore original DATA_FILE
        Reservation.DATA_FILE = cls.original_data_file
        # Delete test file if it exists
        if os.path.exists("test_reservations.json"):
            os.remove("test_reservations.json")

    def setUp(self):
        """Set up test fixtures before each test method."""
        # Clean up before each test
        if os.path.exists(Reservation.DATA_FILE):
            os.remove(Reservation.DATA_FILE)

    def tearDown(self):
        """Clean up after each test method."""
        # Clean up after each test
        if os.path.exists(Reservation.DATA_FILE):
            os.remove(Reservation.DATA_FILE)

    def test_create_reservation_success(self):
        """Test creating a reservation successfully."""
        reservation = Reservation("R001", "C001", "H001")
        result = reservation.create_reservation()
        self.assertTrue(result)

        # Verify reservation was saved
        reservations = Reservation.load_reservations()
        self.assertIn("R001", reservations)
        self.assertEqual(reservations["R001"]["customer_id"], "C001")
        self.assertEqual(reservations["R001"]["hotel_id"], "H001")

    def test_create_reservation_duplicate(self):
        """Test creating a duplicate reservation (negative case)."""
        reservation1 = Reservation("R001", "C001", "H001")
        reservation1.create_reservation()

        # Try to create duplicate
        reservation2 = Reservation("R001", "C002", "H002")
        result = reservation2.create_reservation()
        self.assertFalse(result)

    def test_cancel_reservation_success(self):
        """Test cancelling a reservation successfully."""
        reservation = Reservation("R001", "C001", "H001")
        reservation.create_reservation()

        result = Reservation.cancel_reservation("R001")
        self.assertTrue(result)

        # Verify reservation was cancelled
        reservations = Reservation.load_reservations()
        self.assertNotIn("R001", reservations)

    def test_cancel_reservation_not_found(self):
        """Test cancelling a non-existent reservation (negative case)."""
        result = Reservation.cancel_reservation("R999")
        self.assertFalse(result)

    def test_to_dict(self):
        """Test converting reservation to dictionary."""
        reservation = Reservation("R001", "C001", "H001")
        result = reservation.to_dict()

        self.assertEqual(result["reservation_id"], "R001")
        self.assertEqual(result["customer_id"], "C001")
        self.assertEqual(result["hotel_id"], "H001")

    def test_load_reservations_file_not_exists(self):
        """Test loading reservations when file doesn't exist."""
        reservations = Reservation.load_reservations()
        self.assertEqual(reservations, {})

    def test_load_reservations_invalid_json(self):
        """Test loading reservations with invalid JSON (negative case)."""
        # Create invalid JSON file
        with open(Reservation.DATA_FILE, "w", encoding="utf-8") as f:
            f.write("invalid json content {{{")

        reservations = Reservation.load_reservations()
        self.assertEqual(reservations, {})

    def test_multiple_reservations(self):
        """Test creating multiple reservations."""
        reservation1 = Reservation("R001", "C001", "H001")
        reservation2 = Reservation("R002", "C002", "H001")
        reservation3 = Reservation("R003", "C001", "H002")

        self.assertTrue(reservation1.create_reservation())
        self.assertTrue(reservation2.create_reservation())
        self.assertTrue(reservation3.create_reservation())

        # Verify all reservations exist
        reservations = Reservation.load_reservations()
        self.assertEqual(len(reservations), 3)
        self.assertIn("R001", reservations)
        self.assertIn("R002", reservations)
        self.assertIn("R003", reservations)


if __name__ == "__main__":
    unittest.main()
