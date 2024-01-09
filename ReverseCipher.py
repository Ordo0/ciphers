class ReverseCipher:
    def encode(self, message):
        return message[::-1]

    def decode(self, encoded_message):
        return encoded_message[::-1]