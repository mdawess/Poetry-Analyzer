import unittest, poetry_functions


class TestCleanPoem(unittest.TestCase):
        
    def test_multiple_lines_poem(self):
        """Test clean_poem with a multiple lines poem including empty lines """

        raw_poem = 'The first line leads off,\n\n\nWith a gap before the next.'\
                   '\n    Then the poem ends.\n'
        actual_clean_poem = poetry_functions.clean_poem(raw_poem)
        expected_clean_poem = [['THE', 'FIRST', 'LINE', 'LEADS', 'OFF'],
                               ['WITH', 'A', 'GAP', 'BEFORE', 'THE', 'NEXT'],
                               ['THEN', 'THE', 'POEM', 'ENDS'],
                               ]
        self.assertEqual(actual_clean_poem, expected_clean_poem)
