def get_text_from_book(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def main():
    book_path ="books/frankenstein.txt"
    text = get_text_from_book(book_path)
    print(text)
    num_words = count_words(text)
    print(f"The Number of words in Frankenstein is: {num_words}")

main()