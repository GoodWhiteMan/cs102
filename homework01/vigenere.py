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
                ciphertext += chr((ord(plaintext[g]) - 65 + ord(i) - 65) % 26 + 65)
            elif plaintext[g].islower() and i.islower():
                ciphertext += chr((ord(plaintext[g]) - 97 + ord(i) - 97) % 26 + 97)
            elif plaintext[g].islower() and i.isupper():
                ciphertext += chr((ord(plaintext[g]) - 97 + ord(i) - 65) % 26 + 97)
            elif plaintext[g].isupper() and i.islower():
                ciphertext += chr((ord(plaintext[g]) - 65 + ord(i) - 97) % 26 + 65)
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
                ciphertext += chr((ord(plaintext[g]) - 65 + ord(i) - 65) % 26 + 65)
            elif plaintext[g].islower() and i.islower():
                ciphertext += chr((ord(plaintext[g]) - 97 + ord(i) - 97) % 26 + 97)
            elif plaintext[g].islower() and i.isupper():
                ciphertext += chr((ord(plaintext[g]) - 97 + ord(i) - 65) % 26 + 97)
            elif plaintext[g].isupper() and i.islower():
                ciphertext += chr((ord(plaintext[g]) - 65 + ord(i) - 97) % 26 + 65)
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
                plaintext += chr(((ord(ciphertext[g]) - 65) - (ord(i) - 65)) % 26 + 65)
            elif ciphertext[g].islower() and i.islower():
                plaintext += chr(((ord(ciphertext[g]) - 97) - (ord(i) - 97)) % 26 + 97)
            elif ciphertext[g].islower() and i.isupper():
                plaintext += chr(((ord(ciphertext[g]) - 97) - (ord(i) - 65)) % 26 + 97)
            elif ciphertext[g].isupper() and i.islower():
                plaintext += chr(((ord(ciphertext[g]) - 65) - (ord(i) - 97)) % 26 + 65)
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
                plaintext += chr(((ord(ciphertext[g]) - 65) - (ord(i) - 65)) % 26 + 65)
            elif ciphertext[g].islower() and i.islower():
                plaintext += chr(((ord(ciphertext[g]) - 97) - (ord(i) - 97)) % 26 + 97)
            elif ciphertext[g].islower() and i.isupper():
                plaintext += chr(((ord(ciphertext[g]) - 97) - (ord(i) - 65)) % 26 + 97)
            elif ciphertext[g].isupper() and i.islower():
                plaintext += chr(((ord(ciphertext[g]) - 65) - (ord(i) - 97)) % 26 + 65)
            else:
                plaintext += ciphertext[g]
            g += 1
    return plaintext
