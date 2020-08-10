import unittest, poetry_functions


class TestExtractPhonemes(unittest.TestCase):

    def test_multiple_lines_poem(self):
        """Test extract_phonemes with a multiple lines poem."""

        word_to_phonemes = {'YES': ['Y', 'EH1', 'S'], 'NO': ['N', 'OW1']}
        cleaned_poem = [['YES'], ['NO', 'YES']]
        actual_poem_pronunciation = poetry_functions.extract_phonemes(
            cleaned_poem, word_to_phonemes)
        expected_poem_pronunciation = [[['Y', 'EH1', 'S']], [['N', 'OW1'],
                                                           ['Y', 'EH1', 'S']]]
        self.assertEqual(actual_poem_pronunciation, expected_poem_pronunciation)
