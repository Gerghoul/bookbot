def main():
    from stats import get_num_words

    number_of_words = get_num_words("books/frankenstein.txt")
    print(f"Found {number_of_words} total words")

main()