from string import ascii_lowercase
import random


def key_gen() -> dict[str, str]:
    abecedary = list(ascii_lowercase)
    random.shuffle(abecedary)
    return dict(zip(abecedary, list(ascii_lowercase)))


def encryptor(men: str, key: dict[str, str]) -> str:
    encryp = []
    for letter in men:
        if letter in key.keys():
            encryp.append(key[letter])
        else:
            encryp.append(letter)
    return ''.join(encryp)
