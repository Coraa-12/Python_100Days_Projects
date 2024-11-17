import unittest
from unittest.mock import patch
from io import StringIO
import sys
from roller_coaster import (
    get_validated_numeric_input,
    get_yes_no_input,
    calculate_ticket_price,
    get_ticket_type,
    process_rider,
    main
)

class TestRollerCoaster(unittest.TestCase):
    """Test suite for the roller coaster ticket system."""

    def setUp(self):
        """Set up test environment before each test."""
        self.held_output = StringIO()
        self.original_stdout = sys.stdout
        sys.stdout = self.held_output

    def tearDown(self):
        """Clean up after each test."""
        sys.stdout = self.original_stdout
        self.held_output.close()

    def assert_output_contains(self, expected_output):
        """Helper method to check if output contains expected string."""
        output = self.held_output.getvalue()
        self.assertIn(expected_output, output)

    def test_get_validated_numeric_input_valid(self):
        """Test get_validated_numeric_input with valid input."""
        with patch('builtins.input', return_value='25'):
            result = get_validated_numeric_input("Enter age: ")
            self.assertEqual(result, 25)

    def test_get_validated_numeric_input_invalid(self):
        """Test get_validated_numeric_input with invalid input."""
        with patch('builtins.input', return_value='abc'):
            result = get_validated_numeric_input("Enter age: ")
            self.assertIsNone(result)
            self.assert_output_contains("Please enter a valid number")

    def test_get_validated_numeric_input_out_of_range(self):
        """Test get_validated_numeric_input with out of range input."""
        with patch('builtins.input', return_value='500'):
            result = get_validated_numeric_input("Enter height: ", max_value=250)
            self.assertIsNone(result)
            self.assert_output_contains("Please enter a value between")

    def test_get_yes_no_input_variations(self):
        """Test get_yes_no_input with various valid inputs."""
        test_cases = [
            ('yes', True),
            ('YES', True),
            ('y', True),
            ('no', False),
            ('NO', False),
            ('n', False)
        ]
        
        for input_value, expected in test_cases:
            with self.subTest(input_value=input_value):
                with patch('builtins.input', return_value=input_value):
                    result = get_yes_no_input("Want photo? ")
                    self.assertEqual(result, expected)

    def test_get_yes_no_input_invalid(self):
        """Test get_yes_no_input with invalid input followed by valid input."""
        with patch('builtins.input', side_effect=['maybe', 'yes']):
            result = get_yes_no_input("Want photo? ")
            self.assertTrue(result)
            self.assert_output_contains("Please answer 'yes' or 'no'")

    def test_calculate_ticket_price(self):
        """Test ticket price calculation for different age groups."""
        test_cases = [
            (8, 5),   # Child ticket
            (15, 7),  # Teen ticket
            (25, 12)  # Adult ticket
        ]
        
        for age, expected_price in test_cases:
            with self.subTest(age=age):
                price = calculate_ticket_price(age)
                self.assertEqual(price, expected_price)

    def test_get_ticket_type(self):
        """Test ticket type determination for different ages."""
        test_cases = [
            (8, "children"),
            (15, "teenagers"),
            (25, "adults")
        ]
        
        for age, expected_type in test_cases:
            with self.subTest(age=age):
                ticket_type = get_ticket_type(age)
                self.assertEqual(ticket_type, expected_type)

    def test_process_rider_too_short(self):
        """Test process_rider with insufficient height."""
        with patch('builtins.input', side_effect=['25', '110']):
            success, bill = process_rider()
            self.assertTrue(success)
            self.assertEqual(bill, 0)
            self.assert_output_contains("not tall enough")

    def test_process_rider_adult_with_photo(self):
        """Test process_rider for adult with photo."""
        with patch('builtins.input', side_effect=['25', '180', 'yes']):
            success, bill = process_rider()
            self.assertTrue(success)
            self.assertEqual(bill, 15)  # 12 for adult ticket + 3 for photo

    def test_process_rider_child_no_photo(self):
        """Test process_rider for child without photo."""
        with patch('builtins.input', side_effect=['10', '130', 'no']):
            success, bill = process_rider()
            self.assertTrue(success)
            self.assertEqual(bill, 5)  # 5 for child ticket

    def test_process_rider_invalid_input(self):
        """Test process_rider with invalid input."""
        with patch('builtins.input', side_effect=['abc']):
            success, bill = process_rider()
            self.assertFalse(success)
            self.assertEqual(bill, 0)

    def test_main_function_success(self):
        """Test main function with valid inputs."""
        with patch('builtins.input', side_effect=['25', '180', 'yes']):
            main()
            self.assert_output_contains("Welcome to the Roller Coaster!")
            self.assert_output_contains("Your final bill is $15")
            self.assert_output_contains("Enjoy your ride!")

    def test_main_function_invalid_input(self):
        """Test main function with invalid input."""
        with patch('builtins.input', side_effect=['abc']):
            main()
            self.assert_output_contains("Please enter a valid number")

if __name__ == '__main__':
    unittest.main(verbosity=2)