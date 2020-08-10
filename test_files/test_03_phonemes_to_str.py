import unittest, poetry_functions


class TestPhonemesToStr(unittest.TestCase):

    def test_multiple_lines_poem(self):
        """Test phonemes_to_str with a multiple lines poem."""

        poem_pronunciation = [[['Y', 'EH1', 'S']],
                              [['N', 'OW1'], ['Y', 'EH1', 'S']]
                              ]
        actual_poem_pronunciation_str = poetry_functions.phonemes_to_str(
            poem_pronunciation)
        expected_poem_pronunciation_str = 'Y EH1 S\nN OW1 | Y EH1 S'
        self.assertEqual(actual_poem_pronunciation_str,
                         expected_poem_pronunciation_str)
