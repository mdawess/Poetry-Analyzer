"""Functions for reading the pronouncing dictionary and the poetry forms files
"""
from typing import TextIO

from poetry_constants import (
    CLEAN_POEM, WORD_PHONEMES, LINE_PRONUNCIATION, POEM_PRONUNCIATION,
    PRONOUNCING_DICTIONARY, POETRY_FORM, POETRY_FORMS)

SAMPLE_POETRY_FORM_FILE = '''Limerick
8 A
8 A
5 B
5 B
8 A

Haiku
5 *
7 * 
5 *
'''

EXPECTED_POETRY_FORMS = {
    'Haiku': ([5, 7, 5], ['*', '*', '*']),
    'Limerick': ([8, 8, 5, 5, 8], ['A', 'A', 'B', 'B', 'A'])
}

SAMPLE_FORM_FILE_2 = '''Quintain
0 A
0 B
0 A
0 B
0 B

Rondeau
8 A
8 A
8 B
8 B
8 A
8 A
8 A
8 B
4 C
8 A
8 A
8 B
8 B
8 A
4 C
'''

EXPECTED_FORMS_2 = {
    'Quintain': ([0, 0, 0, 0, 0], ['A', 'B', 'A', 'B', 'B']), 
    'Rondeau': ([8, 8, 8, 8, 8, 8, 8, 8, 4, 8, 8, 8, 8, 8, 4], 
                ['A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'C', 'A', 'A', 'B',
                 'B', 'A', 'C'])
}

SAMPLE_DICTIONARY_FILE = ''';;; Comment line
ABSINTHE  AE1 B S IH0 N TH
HEART  HH AA1 R T
FONDER  F AA1 N D ER0
'''
SAMPLE_DICT_2 = ''';;; Comment line 
YES Y EH1 S
NO N OW1
'''

EXPECTED_DICTIONARY = {
    'ABSINTHE': ['AE1', 'B', 'S', 'IH0', 'N', 'TH'],
    'HEART': ['HH', 'AA1', 'R', 'T'],
    'FONDER': ['F', 'AA1', 'N', 'D', 'ER0']
}

SAMPLE_POEM_FILE = '''  Is this mic on?

Get off my lawn.
'''
EDGE_CASE = """A clumsy young fellow named Tim
was never informed how to swim
He fell off a dock
And that was the wet end of him"""

def read_and_trim_whitespace(poem_file: TextIO) -> str:
    """Return a string containing the poem in poem_file, with
    blank lines and leading and trailing whitespace removed.

    >>> import io
    >>> poem_file = io.StringIO(SAMPLE_POEM_FILE)
    >>> read_and_trim_whitespace(poem_file)
    'Is this mic on?\\nGet off my lawn.'
    >>> poem_file = io.StringIO(EDGE_CASE)
    >>> read_and_trim_whitespace(poem_file)
    'A clumsy young fellow named Tim\\nwas never informed how to swim\\n
    He fell off a dock\\nAnd that was the wet end of him'
    """
    string = ''
    for line in poem_file.readlines():
        if line != '\n':
            string += line
    return string.strip() 


def read_pronouncing_dictionary(
        pronunciation_file: TextIO) -> PRONOUNCING_DICTIONARY:
    """Read pronunciation_file, which is in the format of the CMU Pronouncing
    Dictionary, and return the pronunciation dictionary.

    >>> import io
    >>> dict_file = io.StringIO(SAMPLE_DICTIONARY_FILE)
    >>> result = read_pronouncing_dictionary(dict_file)
    >>> result == EXPECTED_DICTIONARY
    True
    >>> import io
    >>> dict_file = io.StringIO(SAMPLE_DICT_2)
    >>> read_pronouncing_dictionary(dict_file)
    {'YES': ['Y', 'EH1', 'S'], 'NO': ['N', 'OW1']}
    """
    x = separate_file(pronunciation_file)
    
    keys = []
    for lst in x:
        keys.append(lst[0])
        
    values = []
    for word in x:
        values.append(word[1:])
    
    pronouncing_dictionary = {}
    for i in range(len(keys)):
        pronouncing_dictionary[keys[i]] = values[i]
    
    return pronouncing_dictionary

#======================= Pronouncing Dictionary Helpers ========================

def separate_file(pronunciation_file: TextIO) -> CLEAN_POEM:
    """Return a list of lists containing a word and its phonetic 
    pronunciation.
    
    >>> import io
    >>> dict_file = io.StringIO(SAMPLE_DICT_2)
    >>> separate_file(dict_file)
    [['YES', 'Y', 'EH1', 'S'], ['NO', 'N', 'OW1']]
    """
    separated_file = []
    x = pronunciation_file.readlines()
    for item in x: 
        separated_file.append(item.split())
    if separated_file[0][0] == ';;;':
        separated_file.remove(separated_file[0])
    
    return separated_file

def read_poetry_form_descriptions(poetry_forms_file: TextIO) -> POETRY_FORMS:
    """Return a dictionary of poetry form name to poetry pattern for the poetry
    forms in poetry_forms_file.

    >>> import io
    >>> form_file = io.StringIO(SAMPLE_POETRY_FORM_FILE)
    >>> result = read_poetry_form_descriptions(form_file)
    >>> result == EXPECTED_POETRY_FORMS
    True
    >>> import io
    >>> form_file = io.StringIO(SAMPLE_FORM_FILE_2)
    >>> read_poetry_form_descriptions(form_file)
    {'Quintain': ([0, 0, 0, 0, 0], ['A', 'B', 'A', 'B', 'B']), 
    'Rondeau': ([8, 8, 8, 8, 8, 8, 8, 8, 4, 8, 8, 8, 8, 8, 4], 
    ['A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'C', 'A', 'A', 'B', 
    'B', 'A', 'C'])}
    """
    sep = add_to_list(poetry_forms_file)
    
    keys = []
    values = []
    for lst in sep:
        for word in lst:
            if len(word) > 1:
                keys.append(word)
                values.append([])

    separate(sep, values)

    n = 0
    syllables = []
    for lst in values:
        syllables.append([])
        for char in lst:
            if char.isdigit():
                syllables[n].append(int(char))
        n += 1

    k = 0
    rhymes = []
    for lst in values:
        rhymes.append([])
        for char in lst:
            if char.isalpha() or char == '*':
                rhymes[k].append(char)
        k += 1 
    
    return create_dictionary(keys, syllables, rhymes)

#============================= Poetry Form Helpers =============================
def add_to_list(poetry_forms_file: TextIO) -> CLEAN_POEM:
    """Return the poetry_forms_file converted into a list of lists conaining 
    the poem title, syllables and rhyme scheme.
    
    >>> import io
    >>> form_file = io.StringIO(SAMPLE_POETRY_FORM_FILE)
    >>> add_to_list(form_file)
    [['Limerick'], ['8', 'A'], ['8', 'A'], ['5', 'B'], ['5', 'B'], ['8', 'A'], 
    [], ['Haiku'], ['5', '*'], ['7', '*'], ['5', '*']]
    """
    sep = []
    x = poetry_forms_file.readlines()
    for item in x:
        sep.append(item.split())
        
    return sep

def separate(sep: CLEAN_POEM, values: CLEAN_POEM) -> CLEAN_POEM:
    """Return a list containing the syllables and rhyme scheme for each poem 
    type
    
    >>> sep = [['Limerick'], ['8', 'A'], ['8', 'A'], ['5', 'B'], ['5', 'B'], 
    ['8', 'A'], [], ['Haiku'], ['5', '*'], ['7', '*'], ['5', '*']]
    >>> values = [[], []]
    >>> separate(sep, values)
    [['8', 'A', '8', 'A', '5', 'B', '5', 'B', '8', 'A'], 
    ['5', '*', '7', '*', '5', '*']]
    """
    i = 0
    for lst in sep:
        if lst == []:
            i += 1
        for word in lst:
            if len(word) == 1:
                values[i].append(word)
    return values

def create_dictionary(keys: WORD_PHONEMES, syllables: CLEAN_POEM, 
                      rhymes: CLEAN_POEM) -> POETRY_FORMS:
    """Return a dictionary using the poem type as the key and a tuple containing
    the corresponding syllables and rhyme scheme.
    
    >>> import io
    >>> form_file = io.StringIO(SAMPLE_POETRY_FORM_FILE)
    >>> result = read_poetry_form_descriptions(form_file)
    >>> result == EXPECTED_POETRY_FORMS
    True
    """
    poetry_descriptions = {}
    for v in range(len(keys)):
        poetry_descriptions[keys[v]] = syllables[v], rhymes[v]
    
    return poetry_descriptions    