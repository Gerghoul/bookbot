def get_book_text(path_to_file):
    with open(path_to_file, "r", encoding="utf-8") as f:
        file_contents = f.read()
    return file_contents

def get_num_words(path_to_file):
    book = get_book_text(path_to_file)
    words = book.split()
    number_of_words = len(words)
    return number_of_words

def counting_symbols(path_to_file):
    text = get_book_text(path_to_file).lower()
    counts = {}
    for ch in text:
        if ch.isalpha():  # skip non-letters as per assignment
            counts[ch] = counts.get(ch, 0) + 1
    return counts

def sort_on(items):
    return items["num"]

def sorting_counts(path_to_file):
    counts = counting_symbols(path_to_file)
    items = [{"char": ch, "num": n} for ch, n in counts.items()]
    items.sort(key=lambda d: d["num"], reverse=True)
    return items

def print_sorted(path_to_file):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(path_to_file)} total words")
    print("--------- Character Count -------")
    for item in sorting_counts(path_to_file):
        ch = item["char"]
        num = item["num"]
        print(f"{ch}: {num}")
    print("============= END ===============")