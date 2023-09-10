from string import ascii_lowercase
from random import shuffle



message: str = input()

def main(message: str) -> str:
    ascii_lowercase_list: list = [letter for letter in ascii_lowercase]
    ascii_lowercase_list_random: list = ascii_lowercase_list.copy()
    shuffle(ascii_lowercase_list_random)
    final_message: str = ""
    random_letters: dict = { x: y for x, y in zip(ascii_lowercase_list, ascii_lowercase_list_random)}
    for letter in message:
        if letter in ascii_lowercase:
            final_message += random_letters[letter]
    return final_message