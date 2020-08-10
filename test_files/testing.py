import unittest, test_01_clean_poem, test_02_extract_phonemes, \
    test_03_phonemes_to_str, test_04_get_rhyme_scheme, \
    test_05_get_num_syllables, test_06_read_and_trim_whitespace, \
    test_07_read_pronouncing_dictionary, test_08_read_poetry_from_descriptions


test_modules = [
    'test_01_clean_poem',
    'test_02_extract_phonemes',
    'test_03_phonemes_to_str',
    'test_04_get_rhyme_scheme',
    'test_05_get_num_syllables',
    'test_06_read_and_trim_whitespace',
    'test_07_read_pronouncing_dictionary',
    'test_08_read_poetry_from_descriptions',
    ]

# Run all the tests
unittest.main(defaultTest=test_modules, exit=False)

