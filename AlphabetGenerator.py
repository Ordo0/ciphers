class AlphabetGenerator:
    def __init__(self, start_char, end_char):
        self.start_char = start_char
        self.end_char = end_char

    def generate_alphabet(self):
        alphabet = ""
        for char_code in range(ord(self.start_char), ord(self.end_char) + 1):
            alphabet += chr(char_code)
        return alphabet
