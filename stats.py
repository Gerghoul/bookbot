def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(path_to_file):
    book = get_book_text(path_to_file)
    words = book.split()
    number_of_words = len(words)
    return number_of_words

def counting_symbols(path_to_file):
    text = get_book_text(path_to_file)
    lower_case_string = text.lower()
    counting_list = []
    
    for character in lower_case_string:
        character_dict = dict(char = character, num = 1)
        if character_dict not in counting_list:
            counting_list.append(character_dict)
        else:
            character_dict["num"] += 1
            
    return counting_list

def sort_on(items):
    return items["num"]

def sorting_counts(path_to_file):
    counts = counting_symbols(path_to_file)
    sorted_counts = counts.sort(reverse=True, key=sort_on)
    
    return sorted_counts



def print_sorted(path_to_file):
    print(counting_symbols(path_to_file))
    sorted_data = sorting_counts(path_to_file)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    number_of_words = get_num_words(path_to_file)
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    #---actual sorted part---
    print(sorted_data)
    #for symbol in sorted_data:
    #    if symbol.isalpha():
    #        index = sorted_data[symbol]
    #        print(f"{symbol}: {index}")
    #------------------------
    print("============= END ===============")