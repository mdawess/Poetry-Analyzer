import unittest, poetry_functions

class TestGetRhymeScheme(unittest.TestCase):

    def test_multiple_lines_poem_same_rhyme(self):
        """Test get_rhyme_scheme with a multiple lines poem with the same
        rhyme."""

        poem_pronunciation = [[['IH0', 'N']], [['S', 'IH0', 'N']]]
        actual_rhyme_scheme = poetry_functions.get_rhyme_scheme(
            poem_pronunciation)
        expected_rhyme_scheme = ['A', 'A']
        self.assertEqual(actual_rhyme_scheme, expected_rhyme_scheme)
