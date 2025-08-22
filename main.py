import sys
from stats import count_words, character_count, sort_char_counts

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    print("=============== BOOKBOT ===============")
    print(f"Analyzing book found at {filepath}...")
    book_text = get_book_text(filepath)
    num_words = count_words(book_text)
    print("------------------Word Count ----------------")
    print(f"Found {num_words} total words")
    char_counts = character_count(book_text)
    sorted_chars = sort_char_counts(char_counts)
    print("------------- Character Count ------------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("================ END =================")

main()
