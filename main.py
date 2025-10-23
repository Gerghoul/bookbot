def main():
    from stats import print_sorted
    path_to_file = "books/frankenstein.txt"

    print_sorted(path_to_file)
    #print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------\nFound 75767 total words\n--------- Character Count -------\ne: 44538\nt: 29493\na: 25894\no: 24494\ni: 23927\nn: 23643\ns: 20360\nr: 20079\nh: 19176\nd: 16318\nl: 12306\nm: 10206\nu: 10111\nc: 9011\nf: 8451\ny: 7756\nw: 7450\np: 5952\ng: 5795\nb: 4868\nv: 3737\nk: 1661\nx: 691\nj: 497\nq: 325\nz: 235\næ: 28\nâ: 8\nê: 7\në: 2\nô: 1\n============= END ===============")

main()