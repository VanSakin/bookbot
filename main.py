from stats import *

def get_book_text(file_p):
    with open(file_p) as f:
        file_contents = f.read()
    #print(file_contents)
    return file_contents


def main():
    file_path = "books/frankenstein.txt"
    letters = {}
    book = get_book_text(file_path)
    total = word_count(book)
    letters = letter_count(book)
    print(f"{total} words found in the document")
    for i in letters:
        print(f"'{i}': {letters[i]}")

main()
    