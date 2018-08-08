"""
Your mission is to encrypt a secret message (text only, without special chars like "!", "&", "?" etc.)
using Caesar cipher where each letter of input text is replaced by another that stands at a fixed distance.
For example ("a b c", 3) == "d e f"
"""

import string

ALPHABET = string.ascii_lowercase


def to_encrypt(text, delta):
    result = ""
    for letter in text:
        if letter.lower() in ALPHABET:
            pos = ALPHABET.find(letter)
            result += ALPHABET[(pos + delta) % len(ALPHABET)]
        else:
            result += letter
    return result


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")
