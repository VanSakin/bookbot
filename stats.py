#import main

def word_count(words):
    #count the number of words in the book
    #print(words)
    split_words = words.split()
    word_count = len(split_words)
    return word_count