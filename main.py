def main():
    import sys
    from stats import print_sorted
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path_to_file = sys.argv[1]
        print_sorted(path_to_file)

main()