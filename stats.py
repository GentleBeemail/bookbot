def count_words(book_text):
    words = book_text.split()
    num_words = len(words)
    print(f"{num_words} words found in the document")
    return num_words

def character_count(text):
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_char_counts(char_counts):
    char_list = [{"char": char, "num": count} for char, count in char_counts.items() if char.isalpha()]
    def sort_on(item):
        return item["num"]
    char_list.sort(reverse=True, key=sort_on)
    return char_list
