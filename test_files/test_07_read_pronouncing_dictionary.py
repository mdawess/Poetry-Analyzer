import unittest, io, poetry_reader


class TestReadPronouncingDictionary(unittest.TestCase):

    def test_multiple_dict_entries(self):
        """Test read_pronouncing_dictionary with multiple dict entries .
        """

        dict_file = io.StringIO(''';;; Comment line
                                    ABSINTHE  AE1 B S IH0 N TH
                                    HEART  HH AA1 R T
                                    FONDER  F AA1 N D ER0
                                    ''')
        actual_pronouncing_dict = poetry_reader.read_pronouncing_dictionary(
            dict_file)
        expected_pronouncing_dict = {
                            'ABSINTHE': ['AE1', 'B', 'S', 'IH0', 'N', 'TH'],
                            'HEART': ['HH', 'AA1', 'R', 'T'],
                            'FONDER': ['F', 'AA1', 'N', 'D', 'ER0']
                            }
        self.assertEqual(actual_pronouncing_dict, expected_pronouncing_dict)
