import sys

if len(sys.argv) == 2:
    book_path = sys.argv[1]

else:
    pringt("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import get_num_words, get_chars_dict, chars_dict_to_sorted_list

def get_book_text(filepath):
        with open(filepath) as f:
            file_contents =f.read()
        return file_contents


def main():
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    chars_dict = get_chars_dict(book_text)
    sorted_chars = chars_dict_to_sorted_list(chars_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------") 
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()
