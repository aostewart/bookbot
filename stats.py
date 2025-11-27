def get_num_words(text): 
    words = text.split()
    word_count = len(words)
    return word_count

def get_chars_dict(text):
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(char_count):
    return char_count["num"]

def chars_dict_to_sorted_list(char_count):
    result_list = []  # Make an empty list.
    for char, count in char_count.items():  # Loop over the dictionary
        if char.isalpha() == True:
            result_list.append({"char": char, "num": count})  # append dictionaries to the list.
    result_list.sort(reverse=True, key=sort_on)  # Sort the list.
    return result_list  # return the list


