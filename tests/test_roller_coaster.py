# test_roller_coaster2.py
import unittest
from io import StringIO
from unittest.mock import patch
import roller_coaster2


class TestRollerCoaster(unittest.TestCase):

    @patch('builtins.input', side_effect=["150", "10", "yes"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_child_with_photo(self, mock_stdout, mock_input):
        roller_coaster2.main()
        output = mock_stdout.getvalue()
        self.assertIn("You are allowed to ride the roller coaster.", output)
        self.assertIn("The ticket price is $5 for children", output)
        self.assertIn("Photo added to your bill.", output)
        self.assertIn("Your final bill is: $8", output)

    @patch('builtins.input', side_effect=["150", "16", "no"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_teen_without_photo(self, mock_stdout, mock_input):
        roller_coaster2.main()
        output = mock_stdout.getvalue()
        self.assertIn("You are allowed to ride the roller coaster.", output)
        self.assertIn("The ticket price is $7 for teens", output)
        self.assertIn("Your final bill is: $7", output)

    @patch('builtins.input', side_effect=["150", "50", "no"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_senior(self, mock_stdout, mock_input):
        roller_coaster2.main()
        output = mock_stdout.getvalue()
        self.assertIn("You are allowed to ride the roller coaster.", output)
        self.assertIn("The ticket is free for our senior riders", output)
        self.assertIn("Your final bill is: $0", output)

    @patch('builtins.input', side_effect=["115", "25", "yes"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_too_short(self, mock_stdout, mock_input):
        roller_coaster2.main()
        output = mock_stdout.getvalue()
        self.assertIn("You are not allowed to ride the roller coaster.", output)


if __name__ == "__main__":
    unittest.main()
