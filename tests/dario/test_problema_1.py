import dario.Problema_1.problema1 as problem
from string import ascii_lowercase
key = {
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

def test_encryptor():
    assert problem.encryptor("abcdefghijtklmnopqrtsuvwxyz", key) == "htuxlrasgymjkdvwqofminbpzce"


def test_encryptor_empty_message():
    assert problem.encryptor("", key) == ""


def test_encryptor_special_characters():
     assert problem.encryptor("-.,0987654321'¡+ç`´-.,<º ", key) == "-.,0987654321'¡+ç`´-.,<º "


def test_key_gen_has_no_repeated_values():
    keyss = problem.key_gen()
    assert len(keyss.values()) == len(set(keyss.values()))


def test_key_gen_has_all_keys():
    keyss = problem.key_gen()
    assert set(keyss.keys()) == set(ascii_lowercase)


def test_key_gen_has_all_values():
    keyss = problem.key_gen()
    assert set(keyss.keys()) == set(ascii_lowercase)
