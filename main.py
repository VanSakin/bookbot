def get_book_text(file_p):
    with open(file_p) as f:
        file_contents = f.read()
    print(file_contents)
    return file_contents

def main():
    file_path = "books/frankenstein.txt"
    get_book_text(file_path)
    
main()
    