def get_word_count(book_contents):
    book = book_contents.split()
    word_count = len(book)
    return word_count

def intdict(book_string):
    cased = book_string.lower()
    dictionary = {}
    for char in cased:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    return dictionary

def dictexpand(intdict):
    expanded = []
    for i in intdict:
        if i.isalpha():
            dictionary = {}
            dictionary["char"] = i
            dictionary["num"] = intdict[i]
            expanded.append(dictionary)
        else:
            pass
    return expanded