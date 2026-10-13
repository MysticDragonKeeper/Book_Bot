import sys
from stats import get_num_words
from stats import get_chars_dict
from stats import chars_dict_to_sorted_list

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
#define the path
        #path_to_file = "books/frankenstein.txt"
     
    path_to_book = sys.argv[1]
     
        

# pass the path to the function
    word_count = get_num_words(get_book_text(path_to_book))    
    # print(f"Found {word_count} total words")
# print the sorted list of characters
    sorted_list = chars_dict_to_sorted_list(get_chars_dict(get_book_text(path_to_book)))
   #print(sorted_list)
    print_report(path_to_book, word_count, sorted_list)
# accept the path as a parameter
def get_book_text(path):
# use the parameter value 
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def print_report(book_path, word_count, char_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_string, count_number in char_count:
    
        if not char_string.isalpha():
            continue
        print(f"{char_string}: {count_number}")
    print("============= END ===============")

main()