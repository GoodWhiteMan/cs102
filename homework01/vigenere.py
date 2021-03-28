def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    if len(plaintext) == len(keyword):
        g = 0
        for i in keyword:
            if plaintext[g].isupper() and i.isupper():
                if ord(plaintext[g]) + ord(i) > 155:
                    ciphertext += chr(ord(plaintext[g]) + ord(i) - 91)
                else:
                    ciphertext += chr(ord(plaintext[g]) + ord(i) - 65)
            elif plaintext[g].islower() and i.islower():
                if ord(plaintext[g]) + ord(i) > 219:
                    ciphertext += chr(ord(plaintext[g]) + ord(i) - 123)
                else:
                    ciphertext += chr(ord(plaintext[g]) + ord(i) - 97)
            elif plaintext[g].islower() and i.isupper():
                if ord(plaintext[g]) + ord(i) > 187:
                    ciphertext += chr(ord(plaintext[g]) + ord(i) - 91)
                else:
                    ciphertext += chr(ord(plaintext[g]) + ord(i) - 65)
            elif plaintext[g].isupper() and i.islower():
                if ord(plaintext[g]) + ord(i) > 187:
                    ciphertext += chr(ord(plaintext[g]) + ord(i) - 123)
                else:
                    ciphertext += chr(ord(plaintext[g]) + ord(i) - 97)
            else:
                ciphertext += plaintext[g]
            g += 1
    elif len(plaintext) != len(keyword) and len(keyword) != 0:
        g = 0
        while len(plaintext) != len(keyword):
            keyword += keyword[g]
            g += 1
        g = 0
        for i in keyword:
            if plaintext[g].isupper() and i.isupper():
                if ord(plaintext[g]) + ord(i) > 155:
                    ciphertext += chr(ord(plaintext[g]) + ord(i) - 91)
                else:
                    ciphertext += chr(ord(plaintext[g]) + ord(i) - 65)
            elif plaintext[g].islower() and i.islower():
                if ord(plaintext[g]) + ord(i) > 219:
                    ciphertext += chr(ord(plaintext[g]) + ord(i) - 123)
                else:
                    ciphertext += chr(ord(plaintext[g]) + ord(i) - 97)
            elif plaintext[g].islower() and i.isupper():
                if ord(plaintext[g]) + ord(i) > 187:
                    ciphertext += chr(ord(plaintext[g]) + ord(i) - 91)
                else:
                    ciphertext += chr(ord(plaintext[g]) + ord(i) - 65)
            elif plaintext[g].isupper() and i.islower():
                if ord(plaintext[g]) + ord(i) > 187:
                    ciphertext += chr(ord(plaintext[g]) + ord(i) - 123)
                else:
                    ciphertext += chr(ord(plaintext[g]) + ord(i) - 97)
            else:
                ciphertext += plaintext[g]
            g += 1
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    if len(ciphertext) == len(keyword):
        g = 0
        for i in keyword:
            if ciphertext[g].isupper() and i.isupper():
                if ord(ciphertext[g]) - ord(i) < 0:
                    plaintext += chr(ord(ciphertext[g]) - ord(i) + 91)
                else:
                    plaintext += chr(ord(ciphertext[g]) - ord(i) + 65)
            elif ciphertext[g].islower() and i.islower():
                if ord(ciphertext[g]) - ord(i) < 0:
                    plaintext += chr(ord(ciphertext[g]) - ord(i) + 123)
                else:
                    plaintext += chr(ord(ciphertext[g]) - ord(i) + 97)
            elif ciphertext[g].islower() and i.isupper():
                if ord(ciphertext[g]) - ord(i) < 32:
                    plaintext += chr(ord(ciphertext[g]) - ord(i) + 91)
                else:
                    plaintext += chr(ord(ciphertext[g]) - ord(i) + 65)
            elif ciphertext[g].isupper() and ciphertext[g].islower():
                if (ord(ciphertext[g]) - ord(i) + 33) < 0:
                    plaintext += chr(ord(ciphertext[g]) - ord(i) + 123)
                else:
                    plaintext += chr(ord(ciphertext[g]) - ord(i) + 97)
            else:
                plaintext += ciphertext[g]
            g += 1
    elif len(ciphertext) != len(keyword) and len(keyword) != 0:
        g = 0
        while len(ciphertext) != len(keyword):
            keyword += keyword[g]
            g += 1
        g = 0
        for i in keyword:
            if ciphertext[g].isupper() and i.isupper():
                if ord(ciphertext[g]) - ord(i) < 0:
                    plaintext += chr(ord(ciphertext[g]) - ord(i) + 91)
                else:
                    plaintext += chr(ord(ciphertext[g]) - ord(i) + 65)
            elif ciphertext[g].islower() and i.islower():
                if ord(ciphertext[g]) - ord(i) < 0:
                    plaintext += chr(ord(ciphertext[g]) - ord(i) + 123)
                else:
                    plaintext += chr(ord(ciphertext[g]) - ord(i) + 97)
            elif ciphertext[g].islower() and i.isupper():
                if ord(ciphertext[g]) - ord(i) < 32:
                    plaintext += chr(ord(ciphertext[g]) - ord(i) + 91)
                else:
                    plaintext += chr(ord(ciphertext[g]) - ord(i) + 65)
            elif ciphertext[g].isupper() and ciphertext[g].islower():
                if (ord(ciphertext[g]) - ord(i) + 33) < 0:
                    plaintext += chr(ord(ciphertext[g]) - ord(i) + 123)
                else:
                    plaintext += chr(ord(ciphertext[g]) - ord(i) + 97)
            else:
                plaintext += ciphertext[g]
            g += 1
    return plaintext


print(encrypt_vigenere("Hello, world!", "Love"))
print(ord(" "))
