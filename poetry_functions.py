"""Helper functions for the poetry.py program.
"""

from typing import List
from typing import Tuple
from typing import Dict

from poetry_constants import (
    CLEAN_POEM, WORD_PHONEMES, LINE_PRONUNCIATION, POEM_PRONUNCIATION,
    PRONOUNCING_DICTIONARY)

SAMPLE_POEM = '''Teach us, Sprite or Bird,\n
    What sweet thoughts are thine:\n
   I have never heard\n
    Praise of love or wine\n
That panted forth a flood of rapture so divine.'''

EXPECTED_CLEAN_POEM = [['TEACH', 'US', 'SPRITE', 'OR', 'BIRD'], 
                       ['WHAT', 'SWEET', 'THOUGHTS', 'ARE', 'THINE'],
                       ['I', 'HAVE', 'NEVER', 'HEARD'],
                       ['PRAISE', 'OF', 'LOVE', 'OR', 'WINE'],
                       ['THAT', 'PANTED', 'FORTH', 'A', 'FLOOD', 'OF', 
                        'RAPTURE', 'SO', 'DIVINE']]

PHONEME_DICT = {
    'ABSINTHE': ['AE1', 'B', 'S', 'IH0', 'N', 'TH'],
    'HEART': ['HH', 'AA1', 'R', 'T'],
    'FONDER': ['F', 'AA1', 'N', 'D', 'ER0']
}
POEM = [['ABSINTHE'], ['HEART'], ['FONDER']]

EXPECTED = [[['AE1', 'B', 'S', 'IH0', 'N', 'TH']],
            [['HH', 'AA1', 'R', 'T']],
            [['F', 'AA1', 'N', 'D', 'ER0']]]

SAMPLE_PRONOUNCIATION = [[['AE1', 'B', 'S', 'IH0', 'N', 'TH']], 
                         [['M', 'AY1'], ['F', 'EY1', 'V', 'ER0', 'IH0', 'T'],
                          ['D', 'R', 'IH1', 'NG', 'K']]]
SAMPLE_STR = 'AE1 B S IH0 N TH\nM AY1 | F EY1 V ER0 IH0 T | D R IH1 NG K'

# ===================== Helper Functions =====================


def clean_word(s: str) -> str:
    """Return a new string based on s in which all letters have been converted
    to uppercase and whitespace and punctuation characters have been stripped
    from both ends. Inner punctuation and whitespace is left untouched.

    >>> clean_word('Birthday!!!')
    'BIRTHDAY'
    >>> clean_word('  "Quoted?"\\n\\n\\n')
    'QUOTED'
    """

    punctuation = """!"'`@$%^&_-+={}|\\/,;:.-?)([]<>*#\n\t\r """
    result = s.upper().strip(punctuation)
    return result


def clean_poem(raw_poem: str) -> CLEAN_POEM:
    r"""Return the non-blank, non-empty lines of poem, with whitespace removed
    from the beginning and end of each line and all words capitalized.

    >>> clean_poem('The first line leads off,\n\n\nWith a gap before the next.\n    
    Then the poem ends.\n')
    [['THE', 'FIRST', 'LINE', 'LEADS', 'OFF'], 
    ['WITH', 'A', 'GAP', 'BEFORE', 'THE', 'NEXT'], 
    ['THEN', 'THE', 'POEM', 'ENDS']]
    >>> final_form = clean_poem(SAMPLE_POEM)
    >>> final_form == EXPECTED_CLEAN_POEM
    True
    """
    
    ''' Splitting the poem into individual lines '''
    lines = []
    for line in raw_poem.split('\n'):
        if line != '':
            lines.append(line)
    
    ''' Removing whitespace, punctuation and capitalizing each line '''
    clean = []
    for line in lines:
        clean.append(clean_word(line))

    ''' Creating sublists for individual lines '''
    cleaned_poem = []
    i = 0
    for line in clean:
        cleaned_poem.append(line.split())
        i += 1
        
    ''' Filter individual words '''
    for line in cleaned_poem:
        for word in line:
            line[line.index(word)] = clean_word(word)
    return cleaned_poem

def extract_phonemes(
        cleaned_poem: CLEAN_POEM,
        word_to_phonemes: PRONOUNCING_DICTIONARY) -> POEM_PRONUNCIATION:
    """Return a list where each inner list contains the phonemes for the
    corresponding line of cleaned_poem, based on the word_to_phonemes
    pronouncing dictionary.

    >>> word_to_phonemes = {'YES': ['Y', 'EH1', 'S'], 'NO': ['N', 'OW1']}
    >>> extract_phonemes([['YES'], ['NO', 'YES']], word_to_phonemes)
    [[['Y', 'EH1', 'S']], [['N', 'OW1'], ['Y', 'EH1', 'S']]]
    >>> result = extract_phonemes(POEM, PHONEME_DICT)
    >>> result == EXPECTED
    True
    """
    extracted = cleaned_poem
    for sub in extracted:
        for word in sub:
                sub[sub.index(word)] = word_to_phonemes[word]
    return extracted
    
def phonemes_to_str(poem_pronunciation: POEM_PRONUNCIATION) -> str:
    """Return a string containing all the phonemes in each word in each line in
    poem_pronunciation. The phonemes are separated by spaces, the words are
    separated by ' | ', and the lines are separated by '\n'.

    >>> phonemes_to_str([[['Y', 'EH1', 'S']], [['N', 'OW1'], 
    ['Y', 'EH1', 'S']]])
    'Y EH1 S\\nN OW1 | Y EH1 S'
    >>> result = phonemes_to_str(SAMPLE_PRONOUNCIATION)
    >>> result == SAMPLE_STR
    True
    """
    
    new = form_strings(poem_pronunciation)
    add_dividers(new)

    for line in new:
        if new.index(line) != (len(new) - 1):
            line.append('\n')
    
    string = ''
    for sub in new:
        for item in sub:
            string += item
    return string    

#=========================== Pho to Str Helpers ================================
def form_strings(poem_pronunciation: POEM_PRONUNCIATION) -> List[List[str]]:
    """Return a list of lists with the individual phonemes for a single word
    combined into a single string, with phonemes separated by spaces.
    
    >>> form_strings([[['Y', 'EH1', 'S']], [['N', 'OW1'], ['Y', 'EH1', 'S']]])
    [['Y EH1 S'], ['N OW1', 'Y EH1 S']]
    """
    new = []
    i = 0
    for item in poem_pronunciation:
        new.append([])
        for lst in item:
            string = ''
            for pho in lst:
                string += pho + ' '
            new[i].append(string[:-1])
        i += 1
    return new

def add_dividers(new: List[List[str]]) -> None:
    """Return None. Append ' | ' to new between words.
    
    >>> new = [['Y EH1 S'], ['N OW1', 'Y EH1 S']]
    >>> add_dividers(new)
    >>> new
    [['Y EH1 S'], ['N OW1', ' | ', 'Y EH1 S']]
    """
    for line in new:
        if len(line) > 1:
            i = 1
            while i < len(line):
                line.insert(i, ' | ')  
                i += 2    
#===============================================================================

def get_rhyme_scheme(poem_pronunciation: POEM_PRONUNCIATION) -> List[str]:
    """Return a list of last syllables from the poem described by
    poem_pronunction.

    Precondition: poem_pronunciation is not empty and each PHONEMES list
    contains at least one vowel phoneme.

    >>> get_rhyme_scheme([[['IH0', 'N']], [['S', 'IH0', 'N']]])
    ['A', 'A']
    >>> get_rhyme_scheme([[['TH', 'R', 'IY1', 'D', 'IY2']], 
    [['EH1', 'R', 'AH0', 'N', 'S', 'AH0', 'N', 'Z']], 
    [['AE1', 'B', 'AH0', 'G', 'EY2', 'L']]])
    ['A', 'B', 'C']
    """
    
    end_words = get_last_word(poem_pronunciation)
    
    index = record_index(end_words)
    
    last_vowel = []
    for indices in index:
        last_vowel.append(max(indices))
    
    pho_to_end = []
    x = 0 
    for word in end_words:
        pho_to_end.append(word[last_vowel[x]:])
        x += 1

    pairs = []
    nums = []
    pairs.append(pho_to_end[0])
    for vowel in pho_to_end:
        if vowel in pairs:
            nums.append(pairs.index(vowel))
        elif vowel not in pairs:
            pairs.append(vowel)
            nums.append(pairs.index(vowel))
            
    return create_rhyme_scheme(nums)

#========================== Rhyme Scheme Helpers ===============================
def get_last_word(poem_pronunciation: POEM_PRONUNCIATION) -> List[List[str]]:
    """Collect the pronunciation for the last words from each line of the poem,
    add them to a list and return it.
    
    >>> get_last_word([[['IH0', 'N']], [['S', 'IH0', 'N']]])
    [['IH0', 'N'], ['S', 'IH0', 'N']]
    """
    end_words = []
    for sub in poem_pronunciation:
        end_words.append(sub[-1])
    return end_words

def record_index(end_words: List[List[str]]) -> List[List[int]]:
    """Records the index of every vowel phoneme in a word and appends it to a 
    list.
    
    >>> record_index([['IH0', 'N'], ['S', 'IH0', 'N']])
    [[0], [1]]
    """
    index = []
    n = 0 
    for word in end_words:
        index.append([])
        i = 0
        for pho in word:
            if pho[-1].isdigit():
                index[n].append(word.index(pho, i))
                i = word.index(pho) + 1
        n += 1
    return index

def create_rhyme_scheme(nums: List[int]) -> List[str]:
    """Return a rhyme scheme using alphabet based on the numbers in nums.
    
    >>> create_rhyme_scheme([0, 0, 1, 1, 0])
    ['A', 'A', 'B', 'B', 'A']
    """
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    alphabet_soup = []       
    for num in nums:
        alphabet_soup.append(alphabet[num])
    return alphabet_soup    
#===============================================================================

def get_num_syllables(poem_pronunciation: POEM_PRONUNCIATION) -> List[int]:
    """Return a list of the number of syllables in each poem_pronunciation
    line.
    
    >>> get_num_syllables([[['Y', 'EH1', 'S']], [['N', 'OW1'], 
    ['Y', 'EH1', 'S']]])
    [1, 2]
    >>> get_num_syllables(SAMPLE_PRONOUNCIATION)
    [2, 5]
    """
    num_syllables = []
    for line in poem_pronunciation:
        num_syllables.append(count_syllables(line))
        
    return num_syllables

# ======================= Helper Function ========================
def count_syllables(line_pronunciation: LINE_PRONUNCIATION) -> int:
    """ Returns the number of syllables in a single line of poetry.
    
    >>> count_syllables([['N', 'OW1'], ['Y', 'EH1', 'S']])
    2
    >>> count_syllables([['AE1', 'B', 'S', 'IH0', 'N', 'TH']])
    2
    """
    count = 0
    for word in line_pronunciation:
        for pho in word:
            if pho[-1].isdigit():
                count += 1
    return count


if __name__ == '__main__':
    import doctest

    doctest.testmod()
