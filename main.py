def get_text_from_book(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_character_appearance(text):
    character_dict = {}
    text = text.lower()
    for char in text:
        if char not in character_dict:
            character_dict.setdefault(char,1)
        else:
            character_dict[char] += 1
    return character_dict


def main():
    book_path ="books/frankenstein.txt"
    text = get_text_from_book(book_path)
    print(text)
    num_words = count_words(text)
    print(f"The Number of words in Frankenstein is: {num_words}")
    letter_count = count_character_appearance(text)
    print(f"Anzahl der einzlnen Buchstaben: {letter_count}")

main()