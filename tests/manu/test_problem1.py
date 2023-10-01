from manu.problem1.main import create_random_letters, main
from string import ascii_lowercase


def test_key_has_no_repeated_letters():
    rand_letters = create_random_letters()
    assert len(set(rand_letters.values())) == len(rand_letters.values())


def test_encrypt():
    key: dict[str, str] = {'a': 'b', 'l': 'm', 'h': 'i', 'o': 'p'}
    ecrypt_msg_by_function: str = main('hola', key) 
    assert ecrypt_msg_by_function == 'ipmb'


def test_special_caracter_are_not_encrypted():
    key: dict[str, str] = {'a': 'b', 'l': 'm', 'h': 'i', 'o': 'p'}
    ecrypt_msg_by_function: str = main('hola@ #·$', key)
    assert ecrypt_msg_by_function == 'ipmb@ #·$'


def test_included_abecedary_in_key() -> None:
    rand_letters: dict[str, str] = create_random_letters()
    assert set(rand_letters.keys()) == set(ascii_lowercase)
