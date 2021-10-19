"""
File: anagram.py
Name: Max Chang
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'     # Alphabet index

# Global Variables
dictionary = [set() for i in range(26)]
find = []


def main():
    global find
    print('Reading Dictionary...')
    read_dictionary()
    print(f'Welcome to stanCode "Anagram Generator" (or {EXIT} to quit)')
    while True:
        string = input(f"Find anagrams for(or {EXIT} to quit):")
        if string == EXIT:
            break
        tStart = time.time()
        string = string.lower().strip()
        find = []
        find_anagrams(string)
        tEnd = time.time()
        print(f"{len(find)} anagrams: {find}")
        print(f"Use {tEnd - tStart} seconds to find.")


def read_dictionary():
    """
    Read the dictionary file into dictionary global variable
    """
    with open(FILE, 'r') as f:
        for line in f:
            dictionary[ALPHABET.find(line[0])].add(line.lower().strip())


def find_anagrams(s):
    """
    The function to find anagrams, calls different recursion helper function
    based on different length of word
    :param s: (str) the string to find anagrams
    :return: None
    """
    print('Searching...')
    lst = []
    string = []
    lst += s
    for ch in s:
        if ch not in string:
            string.append(ch)
    if len(s) < 12:
        find_anagrams_nocheck(string, '', lst)
    else:
        find_anagrams_check(string, '', lst)


def find_anagrams_nocheck(s, chosen, lst):
    """
    The recursion helper function for string length <12, no early recursion stop
    :param s: (str) filtered original string
    :param chosen: (str) the chosen string
    :param lst: (list) the remaining character
    :return: None
    """
    if len(lst) == 0:
        if chosen in dictionary[ALPHABET.find(chosen[0])]:
            print('Found:', chosen)
            print('Searching...')
            find.append(chosen)
    else:
        for ch in s:
            if ch in lst:
                lst.remove(ch)
                find_anagrams_nocheck(s, chosen + ch, lst)
                lst.append(ch)


def find_anagrams_check(s, chosen, lst):
    """
    The recursion helper function for string length >12, early recursion stop by check pre_fix
    :param s: (str) filtered original string
    :param chosen: (str) the chosen string
    :param lst: (list) the remaining character
    :return: None
    """
    if len(lst) == 0:
        if chosen in dictionary[ALPHABET.find(chosen[0])]:
            print('Found:', chosen)
            print('Searching...')
            find.append(chosen)
    else:
        for ch in s:
            if ch in lst:
                if has_prefix(chosen + ch):
                    lst.remove(ch)
                    find_anagrams_check(s, chosen + ch, lst)
                    lst.append(ch)


def has_prefix(sub_s):
    """
    Predicate function to check if dictionary have word start with sub_s
    :param sub_s: (str) A substring to check if dictionary have words start with sub_s
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    for element in dictionary[ALPHABET.find(sub_s[0])]:
        if element.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
