def main():
    with open("books/frankenstein.txt", "r") as f:
        text = f.read()
        number_of_words = count_words(text)
        characters = count_letter_occurence(text)
        characters_sorted = sort_dictionary(characters)
        print(f"Book Report: Frankenstein by Mary Shelly\nNumber of character{number_of_words}\nOccurences of each character:\n{characters_sorted}\nEnd of report")


def sort_on(d):
    return d["count"]


def count_words(text):
    words = text.split()
    return len(words)


def count_letter_occurence(text):
    text_to_lower = text.lower()
    characters = {}
    for ch in text_to_lower: 
        if ch in characters:
            characters[ch] += 1
        elif ch.isalpha():
            characters[ch] = 1
    return characters


def sort_dictionary(d):
    sorted_list = []
    for ch in d:
        sorted_list.append({"char": ch, "count": d[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


main()
