from dario.problema1.problema1 import encryptor, key_gen
from string import ascii_lowercase


def test_encryptor(key):
    assert encryptor('abcdefghijtklmnopqrtsuvwxyz', key) == 'htuxlrasgymjkdvwqofminbpzce'


def test_encryptor_empty_message(key):
    assert encryptor('', key) == ''


def test_encryptor_special_characters(key):
    assert encryptor('-.,0987654321¡+ç`´-.,<º ', key) == '-.,0987654321¡+ç`´-.,<º '


def test_key_gen_has_no_repeated_values(key):
    keyss = key_gen()
    assert len(keyss.values()) == len(set(keyss.values()))


def test_key_gen_has_all_keys(key):
    keyss = key_gen()
    assert set(keyss.keys()) == set(ascii_lowercase)


def test_key_gen_has_all_values(key):
    keyss = key_gen()
    assert set(keyss.keys()) == set(ascii_lowercase)
