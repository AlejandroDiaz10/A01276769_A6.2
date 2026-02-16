"""Unit tests for Hotel class."""

import unittest
import os
from src.hotel import Hotel


class TestHotel(unittest.TestCase):
    """Test cases for Hotel class."""

    @classmethod
    def setUpClass(cls):
        """Set up test environment once before all tests."""
        # Save original DATA_FILE path
        cls.original_data_file = Hotel.DATA_FILE
        # Use a test-specific file to avoid conflicts with real data
        Hotel.DATA_FILE = "test_hotels.json"

    @classmethod
    def tearDownClass(cls):
        """Clean up after all tests."""
        # Restore original DATA_FILE
        Hotel.DATA_FILE = cls.original_data_file
        # Delete test file if it exists
        if os.path.exists("test_hotels.json"):
            os.remove("test_hotels.json")

    def setUp(self):
        """Set up test fixtures before each test method."""
        # Clean up before each test
        if os.path.exists(Hotel.DATA_FILE):
            os.remove(Hotel.DATA_FILE)

    def tearDown(self):
        """Clean up after each test method."""
        # Clean up after each test
        if os.path.exists(Hotel.DATA_FILE):
            os.remove(Hotel.DATA_FILE)

    def test_create_hotel_success(self):
        """Test creating a hotel successfully."""
        hotel = Hotel("H001", "Grand Hotel", "New York", 100)
        result = hotel.create_hotel()
        self.assertTrue(result)

        # Verify hotel was saved
        hotels = Hotel.load_hotels()
        self.assertIn("H001", hotels)
        self.assertEqual(hotels["H001"]["name"], "Grand Hotel")
        self.assertEqual(hotels["H001"]["total_rooms"], 100)
        self.assertEqual(hotels["H001"]["available_rooms"], 100)

    def test_create_hotel_duplicate(self):
        """Test creating a duplicate hotel (negative case)."""
        hotel1 = Hotel("H001", "Grand Hotel", "New York", 100)
        hotel1.create_hotel()

        # Try to create duplicate
        hotel2 = Hotel("H001", "Another Hotel", "Boston", 50)
        result = hotel2.create_hotel()
        self.assertFalse(result)

    def test_delete_hotel_success(self):
        """Test deleting an existing hotel."""
        hotel = Hotel("H001", "Grand Hotel", "New York", 100)
        hotel.create_hotel()

        result = Hotel.delete_hotel("H001")
        self.assertTrue(result)

        # Verify hotel was deleted
        hotels = Hotel.load_hotels()
        self.assertNotIn("H001", hotels)

    def test_delete_hotel_not_found(self):
        """Test deleting a non-existent hotel (negative case)."""
        result = Hotel.delete_hotel("H999")
        self.assertFalse(result)

    def test_display_hotel_success(self):
        """Test displaying an existing hotel."""
        hotel = Hotel("H001", "Grand Hotel", "New York", 100)
        hotel.create_hotel()

        result = Hotel.display_hotel("H001")
        self.assertIsNotNone(result)
        self.assertEqual(result["hotel_id"], "H001")
        self.assertEqual(result["name"], "Grand Hotel")

    def test_display_hotel_not_found(self):
        """Test displaying a non-existent hotel (negative case)."""
        result = Hotel.display_hotel("H999")
        self.assertIsNone(result)

    def test_modify_hotel_success(self):
        """Test modifying hotel information."""
        hotel = Hotel("H001", "Grand Hotel", "New York", 100)
        hotel.create_hotel()

        result = Hotel.modify_hotel(
            "H001", name="Grand Plaza Hotel", location="Manhattan"
        )
        self.assertTrue(result)

        # Verify modifications
        hotels = Hotel.load_hotels()
        self.assertEqual(hotels["H001"]["name"], "Grand Plaza Hotel")
        self.assertEqual(hotels["H001"]["location"], "Manhattan")

    def test_modify_hotel_not_found(self):
        """Test modifying a non-existent hotel (negative case)."""
        result = Hotel.modify_hotel("H999", name="Ghost Hotel")
        self.assertFalse(result)

    def test_reserve_room_success(self):
        """Test reserving a room successfully."""
        hotel = Hotel("H001", "Grand Hotel", "New York", 100)
        hotel.create_hotel()

        result = Hotel.reserve_room("H001", "R001")
        self.assertTrue(result)

        # Verify room was reserved
        hotels = Hotel.load_hotels()
        self.assertEqual(hotels["H001"]["available_rooms"], 99)
        self.assertIn("R001", hotels["H001"]["reservations"])

    def test_reserve_room_hotel_not_found(self):
        """Test reserving room in non-existent hotel (negative case)."""
        result = Hotel.reserve_room("H999", "R001")
        self.assertFalse(result)

    def test_reserve_room_no_availability(self):
        """Test reserving room when no rooms available (negative case)."""
        hotel = Hotel("H001", "Small Hotel", "Boston", 1)
        hotel.create_hotel()

        # Reserve the only room
        Hotel.reserve_room("H001", "R001")

        # Try to reserve when no rooms available
        result = Hotel.reserve_room("H001", "R002")
        self.assertFalse(result)

    def test_cancel_reservation_success(self):
        """Test cancelling a reservation successfully."""
        hotel = Hotel("H001", "Grand Hotel", "New York", 100)
        hotel.create_hotel()
        Hotel.reserve_room("H001", "R001")

        result = Hotel.cancel_reservation("H001", "R001")
        self.assertTrue(result)

        # Verify reservation was cancelled
        hotels = Hotel.load_hotels()
        self.assertEqual(hotels["H001"]["available_rooms"], 100)
        self.assertNotIn("R001", hotels["H001"]["reservations"])

    def test_cancel_reservation_hotel_not_found(self):
        """Test cancelling reservation in non-existent hotel (negative)."""
        result = Hotel.cancel_reservation("H999", "R001")
        self.assertFalse(result)

    def test_cancel_reservation_not_found(self):
        """Test cancelling non-existent reservation (negative case)."""
        hotel = Hotel("H001", "Grand Hotel", "New York", 100)
        hotel.create_hotel()

        result = Hotel.cancel_reservation("H001", "R999")
        self.assertFalse(result)

    def test_load_hotels_file_not_exists(self):
        """Test loading hotels when file doesn't exist."""
        hotels = Hotel.load_hotels()
        self.assertEqual(hotels, {})

    def test_load_hotels_invalid_json(self):
        """Test loading hotels with invalid JSON (negative case)."""
        # Create invalid JSON file
        with open(Hotel.DATA_FILE, "w", encoding="utf-8") as f:
            f.write("invalid json content {{{")

        hotels = Hotel.load_hotels()
        self.assertEqual(hotels, {})


if __name__ == "__main__":
    unittest.main()
