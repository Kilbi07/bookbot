def get_text_from_book(path):
    with open(path) as f:
        return f.read()

def main():
    book_path ="books/frankenstein.txt"
    text = get_text_from_book(book_path)
    print(text)

main()