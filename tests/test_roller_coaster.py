# test_roller_coaster.py

import unittest
from unittest.mock import patch
from io import StringIO
from roller_coaster import main

class TestRollerCoasterTicket(unittest.TestCase):
    
    @patch('builtins.input', side_effect=[10, 130, 'yes'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_child_with_photo(self, mock_stdout, mock_input):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("You are tall enough to ride the roller coaster.", output)
        self.assertIn("Ticket is $5 for children", output)
        self.assertIn("Your final bill is $8", output)

    @patch('builtins.input', side_effect=[16, 150, 'no'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_teenager_without_photo(self, mock_stdout, mock_input):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("You are tall enough to ride the roller coaster.", output)
        self.assertIn("Ticket is $7 for teenagers", output)
        self.assertIn("Your final bill is $7", output)

    @patch('builtins.input', side_effect=[22, 140, 'no'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_adult_without_photo(self, mock_stdout, mock_input):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("You are tall enough to ride the roller coaster.", output)
        self.assertIn("Ticket is $12 for adults", output)
        self.assertIn("Your final bill is $12", output)

    @patch('builtins.input', side_effect=[8, 130, 'yes'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_underage_with_photo(self, mock_stdout, mock_input):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("You are tall enough to ride the roller coaster.", output)
        self.assertIn("Ticket is $5 for children", output)
        self.assertIn("Your final bill is $8", output)

    @patch('builtins.input', side_effect=['abc', 130])
    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_age_input(self, mock_stdout, mock_input):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("A ValueError occurred", output)

    @patch('builtins.input', side_effect=[25, 110, 'no'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_not_tall_enough(self, mock_stdout, mock_input):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("You are not tall enough to ride the roller coaster.", output)


if __name__ == '__main__':
    unittest.main()
