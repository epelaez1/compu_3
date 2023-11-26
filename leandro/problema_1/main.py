from random import shuffle
from string import ascii_lowercase


def encrypt(msg: str, key: dict[str, str]) -> str:
    return ''.join(key[letter] for letter in msg)


def generate_key() -> dict[str, str]:
    randomized_alphabet = list(ascii_lowercase)
    shuffle(randomized_alphabet)
    return dict(zip(ascii_lowercase, randomized_alphabet))
