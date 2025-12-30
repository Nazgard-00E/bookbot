from stats import get_num_words, get_character_count, sorted_character_count
import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    num_words = get_num_words((book_text).split())
   
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("-------- Character Count -------")
    for item in sorted_character_count(book_text).items():
        if item[0].isalpha():
            print(f"{item[0]}: {item[1]}")
    print("============= END ===============")
    print(sys.argv)
    


main() 