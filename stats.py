#import main

def word_count(words):
    #count the number of words in the book
    #print(words)
    split_words = words.split()
    word_count = len(split_words)
    return word_count

def letter_count(words):
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",".",","," ","!","?"]
    lower_words = words.lower()
    letters_check = {}
    for i in range(len(letters)):
        counter = 0
        if letters[i] in lower_words:
            for n in range(len(words)):
                if words[n] == letters[i]:
                    counter += 1
            letters_check[letters[i]] = counter
    #print(lower_words)
    return letters_check