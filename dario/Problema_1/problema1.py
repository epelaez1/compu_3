from string import ascii_lowercase
import random


def key_gen() -> dict[str, str]:
    abecedary = list(ascii_lowercase)
    random.shuffle(abecedary)
    return dict(zip(abecedary, list(ascii_lowercase)))


def encryptor(men: str, key: dict[str, str]) -> str:
    encryp = []
    for letter in men:
        encryp.append(key.get(letter, letter))
    return ''.join(encryp)
