def solution(cipher):
    """
        Args:
            cipher(str): a string of uppercase letters
        Return:
            str: the decrypted string
    """

    plain = ""
    for char in cipher:
        if char.isalpha() and not char.isupper():
            offset = 2 * (ord(char) - 97 - 13)
            offset = -abs(offset) - 1 if offset > 0 else abs(offset) - 1
            plain += chr(ord(char) + offset)

        else:
            plain += char

    return plain
