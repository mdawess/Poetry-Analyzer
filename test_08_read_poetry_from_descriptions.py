import unittest, io, poetry_reader


class TestReadPoetryFormDescriptions(unittest.TestCase):

    def test_multiple_forms(self):
        """Test read_poetry_form_descriptions with multiple poetry forms.
        """

        form_file = io.StringIO('''Limerick
                                    8 A
                                    8 A
                                    5 B
                                    5 B
                                    8 A

                                    Haiku
                                    5 *
                                    7 * 
                                    5 *
                                    ''')
        actual_poetry_forms = poetry_reader.read_poetry_form_descriptions(
            form_file)
        expected_poetry_forms = {'Haiku': ([5, 7, 5], ['*', '*', '*']),
                                 'Limerick': ([8, 8, 5, 5, 8],
                                              ['A', 'A', 'B', 'B', 'A'])}
        self.assertEqual(actual_poetry_forms, expected_poetry_forms)
