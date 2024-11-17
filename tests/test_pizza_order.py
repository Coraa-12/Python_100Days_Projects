import unittest
from io import StringIO
from unittest.mock import patch
from pizza_order import calculate_total, get_valid_input

class TestPizzaOrder(unittest.TestCase):
    """Test cases for pizza ordering system"""

    def setUp(self):
        self.maxDiff = None
        
    def test_calculate_total_small_pizza_no_toppings(self):
        total = calculate_total("S", "N", "N")
        self.assertEqual(total, 15)

    def test_calculate_total_large_all_toppings(self):
        total = calculate_total("L", "Y", "Y")
        self.assertEqual(total, 29)

    def test_calculate_total_case_insensitive(self):
        total = calculate_total("s", "y", "y")
        self.assertEqual(total, 18)

    def test_calculate_total_invalid_size(self):
        with self.assertRaises(ValueError):
            calculate_total("XL", "N", "N")

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['S'])
    def test_get_valid_input_valid_size(self, mock_input, mock_stdout):
        result = get_valid_input("Enter size: ", {'S', 'M', 'L'})
        self.assertEqual(result, 'S')

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['X', 'S'])
    def test_get_valid_input_invalid_then_valid(self, mock_input, mock_stdout):
        result = get_valid_input("Enter size: ", {'S', 'M', 'L'})
        self.assertEqual(result, 'S')

if __name__ == '__main__':
    unittest.main(verbosity=0, buffer=True)