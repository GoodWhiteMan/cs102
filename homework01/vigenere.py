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
            if 65 <= ord(plaintext[g]) <= 90 and 65 <= ord(i) <= 90:
                if ord(plaintext[g]) + ord(i) > 155:
                    ciphertext += chr(ord(plaintext[g]) + ord(i) - 91)
                else:
                    ciphertext += chr(ord(plaintext[g]) + ord(i) - 65)
            elif 97 <= ord(plaintext[g]) <= 122 and 97 <= ord(i) <= 122:
                if ord(plaintext[g]) + ord(i) > 219:
                    ciphertext += chr(ord(plaintext[g]) + ord(i) - 123)
                else:
                    ciphertext += chr(ord(plaintext[g]) + ord(i) - 97)
            elif 97 <= ord(plaintext[g]) <= 122 and 65 <= ord(i) <= 90:
                if ord(plaintext[g]) + ord(i) > 187:
                    ciphertext += chr(ord(plaintext[g]) + ord(i) - 91)
                else:
                    ciphertext += chr(ord(plaintext[g]) + ord(i) - 65)
            elif 65 <= ord(plaintext[g]) <= 90 and 97 <= ord(i) <= 122:
                if ord(plaintext[g]) + ord(i) > 187:
                    ciphertext += chr(ord(plaintext[g]) + ord(i) - 123)
                else:
                    ciphertext += chr(ord(plaintext[g]) + ord(i) - 97)
            g += 1
    elif len(plaintext) != len(keyword) and len(keyword) != 0:
        g = 0
        while len(plaintext) != len(keyword):
            keyword += keyword[g]
            g += 1
        g = 0
        for i in keyword:
            if 65 <= ord(plaintext[g]) <= 90 and 65 <= ord(i) <= 90:
                if ord(plaintext[g]) + ord(i) > 155:
                    ciphertext += chr(ord(plaintext[g]) + ord(i) - 91)
                else:
                    ciphertext += chr(ord(plaintext[g]) + ord(i) - 65)
            elif 97 <= ord(plaintext[g]) <= 122 and 97 <= ord(i) <= 122:
                if ord(plaintext[g]) + ord(i) > 219:
                    ciphertext += chr(ord(plaintext[g]) + ord(i) - 123)
                else:
                    ciphertext += chr(ord(plaintext[g]) + ord(i) - 97)
            elif 97 <= ord(plaintext[g]) <= 122 and 65 <= ord(i) <= 90:
                if ord(plaintext[g]) + ord(i) > 187:
                    ciphertext += chr(ord(plaintext[g]) + ord(i) - 91)
                else:
                    ciphertext += chr(ord(plaintext[g]) + ord(i) - 65)
            elif 65 <= ord(plaintext[g]) <= 90 and 97 <= ord(i) <= 122:
                if ord(plaintext[g]) + ord(i) > 187:
                    ciphertext += chr(ord(plaintext[g]) + ord(i) - 123)
                else:
                    ciphertext += chr(ord(plaintext[g]) + ord(i) - 97)
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
            if 65 <= ord(ciphertext[g]) <= 90 and 65 <= ord(i) <= 90:
                if ord(ciphertext[g]) - ord(i) < 0:
                    plaintext += chr(ord(ciphertext[g]) - ord(i) + 91)
                else:
                    plaintext += chr(ord(ciphertext[g]) - ord(i) + 65)
            elif 97 <= ord(ciphertext[g]) <= 122 and 97 <= ord(i) <= 122:
                if ord(ciphertext[g]) - ord(i) < 0:
                    plaintext += chr(ord(ciphertext[g]) - ord(i) + 123)
                else:
                    plaintext += chr(ord(ciphertext[g]) - ord(i) + 97)
            elif 97 <= ord(ciphertext[g]) <= 122 and 65 <= ord(i) <= 90:
                if ord(ciphertext[g]) - ord(i) < 32:
                    plaintext += chr(ord(ciphertext[g]) - ord(i) + 91)
                else:
                    plaintext += chr(ord(ciphertext[g]) - ord(i) + 65)
            elif 65 <= ord(ciphertext[g]) <= 90 and 97 <= ord(i) <= 122:
                if (ord(ciphertext[g]) - ord(i) + 33) < 0:
                    plaintext += chr(ord(ciphertext[g]) - ord(i) + 123)
                else:
                    plaintext += chr(ord(ciphertext[g]) - ord(i) + 97)
            g += 1
    elif len(ciphertext) != len(keyword) and len(keyword) != 0:
        g = 0
        while len(ciphertext) != len(keyword):
            keyword += keyword[g]
            g += 1
        g = 0
        for i in keyword:
            if 65 <= ord(ciphertext[g]) <= 90 and 65 <= ord(i) <= 90:
                if ord(ciphertext[g]) - ord(i) < 0:
                    plaintext += chr(ord(ciphertext[g]) - ord(i) + 91)
                else:
                    plaintext += chr(ord(ciphertext[g]) - ord(i) + 65)
            elif 97 <= ord(ciphertext[g]) <= 122 and 97 <= ord(i) <= 122:
                if ord(ciphertext[g]) - ord(i) < 0:
                    plaintext += chr(ord(ciphertext[g]) - ord(i) + 123)
                else:
                    plaintext += chr(ord(ciphertext[g]) - ord(i) + 97)
            elif 97 <= ord(ciphertext[g]) <= 122 and 65 <= ord(i) <= 90:
                if ord(ciphertext[g]) - ord(i) < 32:
                    plaintext += chr(ord(ciphertext[g]) - ord(i) + 91)
                else:
                    plaintext += chr(ord(ciphertext[g]) - ord(i) + 65)
            elif 65 <= ord(ciphertext[g]) <= 90 and 97 <= ord(i) <= 122:
                if (ord(ciphertext[g]) - ord(i) + 33) < 0:
                    plaintext += chr(ord(ciphertext[g]) - ord(i) + 123)
                else:
                    plaintext += chr(ord(ciphertext[g]) - ord(i) + 97)
            g += 1
    return plaintext
