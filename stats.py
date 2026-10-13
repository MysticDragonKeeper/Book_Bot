def get_num_words(book_text):
    words = book_text.split()
   
    return len(words)
 
def get_chars_dict(book_text):
    unique_chars = {}
    for char in book_text:
        char = char.lower()
        if char in unique_chars:
            unique_chars[char] += 1
        else:
            unique_chars[char] = 1
    return unique_chars

def sort_on(unique_chars: tuple[str, int]) -> int:
    return unique_chars[1]

def chars_dict_to_sorted_list(chars_dict):
    char_list = []
    for char, count in chars_dict.items():
    # Convert the dictionary to a list of tuples
        char_list.append((char, count))
    # Sort the list by the second element of each tuple (the count)
    sorted_list = sorted(char_list, key=sort_on, reverse=True)
    return sorted_list