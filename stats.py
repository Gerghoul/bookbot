def get_book_text (path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(path_to_file):
    book = get_book_text(path_to_file)
    words = book.split()
    number_of_words = len(words)
    return number_of_words