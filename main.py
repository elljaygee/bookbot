def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()


def get_num_words(text):
    words = text.split()
    
    counter = 0
    for word in words:
        counter += 1
    return counter

    # boot.dev solution:
    # words = text.split()
    # return len(words)


def character_count(text):
    book_string = text.strip("")
    book_string_lower = book_string.lower()
    character_dict = {}
    
    for letter in book_string_lower:
        if letter in character_dict:
            character_dict[letter] += 1
        else:
            character_dict[letter] = 1
    return character_dict

def character_sort(text):
    letters = {}
    for l in text.lower():
        if l.isalpha():
            letters[l] = (letters.get(l, 0)) + 1
    
    letters_list = list(letters.items())
    
    sorted_letters = sorted(letters_list, key=lambda tup: tup[1], reverse=True)

    return sorted_letters


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_dict = character_count(text)
    letter_count = character_sort(text)
    print(f"{num_words} words found in the document")
    print(f"The count of each letter in the document is: {character_dict}")
    for key, value in letter_count:
        print(f"The character '{key}' occurs {value} times")
    



if __name__ == "__main__":
    main()
