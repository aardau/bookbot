#main function that will run my other functions
def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book(book_path)
    word_count = get_word_count(book_text)
    char_count = get_char_count(book_text)
    char_sorted = get_char_sorted(char_count)

    #print the report
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()
    for char in char_sorted:
        if not char["char"].isalpha():
            continue
        print(f"The '{char['char']}' character was found {char['num']} times")

    print("-- End report --")


#fetches contents of book
def get_book(filepath):
    with open(filepath) as f:
        return f.read()


#count the words in the book
def get_word_count(text):
    words = text.split()
    return len(words)

#count the characters in the book
def get_char_count(words):
    lowercase_string = words.lower() #turn words into lowercase string
    character_list = {} #initialize dictionary
    for character in lowercase_string:
        if character not in character_list:
            character_list[character] = 1
        else:
            character_list[character] += 1
    return character_list

#used for .sort func
def sort_on(dict):
    return dict["num"]

#sort and order the character count
def get_char_sorted(char_count):
    sorted_list = []
    for char in char_count:
        sorted_list.append({"char": char, "num": char_count[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


#run main function
main()

