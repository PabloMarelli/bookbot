

path_to_file = "books/frankenstein.txt"


def sort_on(dict):
    return dict["num"]


def count_words(book: str) -> str:
    number_of_words = book.split()
    return len(number_of_words)


def count_characters(book: str) -> dict[str:int]:
    characters_count = {}

    lower_book = book.lower()

    for char in lower_book:
        if not char.isalpha():
            continue
        if char in characters_count:
            characters_count[char] += 1
        else:
            characters_count[char] = 1

    return characters_count


def get_report(path_to_file: str, book: str) -> None:
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{count_words(book)} found in the document \n")

    characters_count = count_characters(book)

    for key, value in characters_count.items():
        print(f"The '{key}' character was found {value} times")

    print("--- End report ---")

def main():
    with open(path_to_file) as f:
        file_contents = f.read()

    get_report(path_to_file, file_contents)


main()
