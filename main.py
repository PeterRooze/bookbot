
book = "books/frankenstein.txt"

def main():
    text = read_book(book)
    amount_words = count_words(text)
    number_chars = num_chars(text)
    print(f"--- Begin report of {book} ---")  
    print(f"Total number of words found: {amount_words}")
 #   print(f"Amount of chars: {number_chars}")
    amount_char_overview(number_chars)
    print("--- End report ---")

def count_words(text):
    words = text.split()
    return len(words)

def read_book(path):
    with open(path) as f:
        return f.read()

def num_chars(text):
    dict = {}
    lowered_text = text.lower()
    for text in lowered_text:
        if text in dict:
            dict[text] = dict[text] + 1
        else:
            dict[text] = 1
    return dict

def amount_char_overview(chars):
    sorted_items = sorted(chars.items(), key=lambda item: item[1], reverse=True)
    for letter, amount in sorted_items:
        if letter.isalpha():
            print(f"The {letter} was found {amount} times")

main()  

