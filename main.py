from stats import get_word_count
from stats import intdict
from stats import dictexpand
import sys

def main(book):
    word_count = get_word_count(get_book_text(book))
    #print(f"{word_count} words found in the document")
    diction = intdict(get_book_text(book))
    #print(diction)
    detailed_dictionary = dictexpand(diction)
    detailed_dictionary.sort(reverse=True, key=sort_on)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    for i in detailed_dictionary:
        print(f"{i['char']}: {i['num']}")
    return

def get_book_text(book_path):
    with open(book_path) as file:
        book_contents = file.read()
    return book_contents

def sort_on(items):
    return items["num"]


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main(sys.argv[1])