import pytest


@pytest.fixture
def key() -> dict[str, str]:
    return {
        'g': 'a',
        'v': 'b',
        'y': 'c',
        'm': 'd',
        'z': 'e',
        'r': 'f',
        'i': 'g',
        'a': 'h',
        's': 'i',
        'k': 'j',
        'l': 'k',
        'e': 'l',
        't': 'm',
        'u': 'n',
        'q': 'o',
        'w': 'p',
        'p': 'q',
        'f': 'r',
        'h': 's',
        'b': 't',
        'c': 'u',
        'n': 'v',
        'o': 'w',
        'd': 'x',
        'j': 'y',
        'x': 'z',
    }
