import sys
from stats import get_num_words, get_num_chars, get_sorted, print_analysis_of_book

def get_book_text(fp):
    f = None
    contents = " "
    with open(fp) as f:
        print(f"Analyzing book found at {fp}...")
        contents = f.read()
    return contents



def main():
    file_path = ""
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_path = sys.argv[1]
    print(f"============ BOOKBOT ============")
    #file_path = "books/frankenstein.txt"
    #print(f"{get_book_text(file_path)}")
    book = get_book_text(file_path)
    
    print(f"Found {get_num_words(book)} total words")
    #print(f"{get_num_chars(book)}")
    #print(f"{get_sorted(get_num_chars(book))}")
    print_analysis_of_book(get_sorted(get_num_chars(book)))
    return 0

main()