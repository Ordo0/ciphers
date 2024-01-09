class CaesarCipher:
    def __init__(self, shift, alphabet):
        self.shift = shift
        self.alphabet = alphabet

    def encode(self, message):
        encoded_message = ""
        for char in message:
            if char in self.alphabet:
                char_index = self.alphabet.index(char)
                encoded_index = (char_index + self.shift) % len(self.alphabet)
                encoded_char = self.alphabet[encoded_index]
                encoded_message += encoded_char
            else:
                encoded_message += char
        return encoded_message

    def decode(self, encoded_message):
        decoded_message = ""
        for char in encoded_message:
            if char in self.alphabet:
                char_index = self.alphabet.index(char)
                decoded_index = (char_index - self.shift) % len(self.alphabet)
                decoded_char = self.alphabet[decoded_index]
                decoded_message += decoded_char
            else:
                decoded_message += char
        return decoded_message
