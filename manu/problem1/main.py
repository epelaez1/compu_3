import string
import random


def create_random_letters() -> dict[str, str]:
    random_letters: list[str] = list(string.ascii_lowercase)
    random.shuffle(random_letters)
    return dict(zip(string.ascii_lowercase, random_letters))


def main(message: str, key: dict[str, str]) -> str:
    final_message: list[str] = []
    for letter in message:
        final_message.append(key.get(letter, letter))
    return ''.join(final_message)
