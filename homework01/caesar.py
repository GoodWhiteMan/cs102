import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for i in plaintext:
        if 65 <= ord(i) <= 87 or 97 <= ord(i) <= 119:
            ciphertext += chr(ord(i) + shift)
        elif 91 <= (ord(i) + shift) <= 93:
            ciphertext += chr(64 + ((ord(i) + shift) - 90))
        elif 123 <= (ord(i) + shift) <= 125:
            ciphertext += chr(96 + ((ord(i) + shift) - 122))
        else:
            ciphertext += i
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for i in ciphertext:
        if 68 <= ord(i) <= 90 or 100 <= ord(i) <= 122:
            plaintext += chr(ord(i) - shift)
        elif 62 <= ord(i) <= 67:
            plaintext += chr(91 + ((ord(i) - 65) - shift))
        elif 95 <= ord(i) <= 99:
            plaintext += chr(123 + ((ord(i) - 97) - shift))
        else:
            plaintext += i
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
