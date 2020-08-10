import unittest, poetry_functions


class TestGetNumSyllables(unittest.TestCase):

    def test_multiple_line_poem_same_num(self):
        """Test get_num_syllables with a one line poem."""

        poem_pronunciation = [[['IH0', 'N']], [['S', 'IH0', 'N']]]
        actual_num_syllables = poetry_functions.get_num_syllables(
            poem_pronunciation)
        expected_num_syllables = [1, 1]
        self.assertEqual(actual_num_syllables, expected_num_syllables)
