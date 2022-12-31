def caesarCipherEncryptor(string, key):
    encrypted_msg = ""
    for char in string:
        encrypted_msg += chr((ord(char) + key - 97) % 26 + 97)
    return encrypted_msg