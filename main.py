def get_book_text(file_p):
    with open(file_p) as f:
        file_contents = f.read()
    #print(file_contents)
    return file_contents

def word_count(words):
    #count the number of words in the book
    #print(words)
    split_words = words.split()
    word_count = len(split_words)
    return word_count


def main():
    file_path = "books/frankenstein.txt"
    book = get_book_text(file_path)
    total = word_count(book)
    print(f"{total} words found in the document")
    
main()
    