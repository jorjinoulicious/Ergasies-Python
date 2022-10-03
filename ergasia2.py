def ROT13(string):

    result = ""

    for char in string:
        char_to_dec = ord(char) + 13
        if (char_to_dec <= 90):
            dec_to_char = chr(char_to_dec)
        elif (110<=char_to_dec<=122):
            dec_to_char = chr(char_to_dec)
        else:
            char_to_dec = char_to_dec - 26
            dec_to_char = chr(char_to_dec)

        result += dec_to_char

    return result
