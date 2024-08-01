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

def sort_dict_descending(my_dict):
    my_dict = sorted(my_dict.items(), key=lambda x:x[1], reverse=True)
    sorted_dict = dict(my_dict)
    return sorted_dict

def print_report(book_path):
    report=""
    text = get_text_from_book(book_path)
    num_words = count_words(text)
    character_count = count_character_appearance(text)
    sorted_character_count = sort_dict_descending(character_count)
    report += f"--- Begin report of {book_path} ---\n {num_words} words found in the document\n\n"
    for k,v in sorted_character_count.items():
        if k.isalpha():
            report+=f"The '{k}' character was found {v} times\n"
    report+="--- End report ---"
    print(report)

def main():
    print_report("books/frankenstein.txt")

main()