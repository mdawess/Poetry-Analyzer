import unittest, io, poetry_reader


class TestReadAndTrimWhitespace(unittest.TestCase):

    def test_mix_input(self):
        """Test read_and_trim_whitespace with an input with multiple lines, each
        have leading and trailing whitespaces.
        """

        poem_file = io.StringIO('  Is this mic on?   \n \n   Get off my lawn. ')
        actual_trimmed_poem = poetry_reader.read_and_trim_whitespace(poem_file)
        expected_trimmed_poem = 'Is this mic on?\nGet off my lawn.'
        self.assertEqual(actual_trimmed_poem, expected_trimmed_poem)
