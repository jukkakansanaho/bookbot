from collections import defaultdict
import re

path_to_file = "books/frankenstein.txt"

def count_words(text):
    return len(text.split())

def count_chars(text):
    '''
    Ref-1 (count chars): https://datagy.io/python-count-words/
    Ref-2 (defaultdict): https://datagy.io/python-defaultdict/
    Ref-3 (defaultdict): https://www.geeksforgeeks.org/defaultdict-in-python/
    Ref-4 (re): https://docs.python.org/3/library/re.html
    Ref-5 (sort dict): https://www.geeksforgeeks.org/sort-python-dictionary-by-value/
    '''
    char_counts = defaultdict(int)
    # [a-zA-Z]: alphabets, lowercase and uppercase
    # \w: Matches Unicode word characters; 
    #   this includes all Unicode alphanumeric characters (as defined by str.isalnum()), as well as the underscore (_).
    # \S: Matches any character which is not a whitespace character. This is the opposite of \s.
    for char in re.findall('[a-zA-Z]', text):
        char = char.lower()
        char_counts[char] +=1
    sorted_dict = {}
    for key in sorted(char_counts, key=char_counts.get, reverse=True):
        sorted_dict[key] = char_counts[key]
    return sorted_dict

def form_report(word_count, char_dict): 
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{word_count} word found in the document\n")
    for key in char_dict.keys():
        print(f"The '{key}' character was found {char_dict[key]} times")
    print(f"--- End report ---")

def main():
    with open(path_to_file) as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        char_counts = count_chars(file_contents)
        form_report(word_count, char_counts)

main()