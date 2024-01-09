import base64


class Base64Cipher:
    def encode(self, message):
        encoded_bytes = base64.b64encode(message.encode('utf-8'))
        encoded_message = encoded_bytes.decode('utf-8')
        return encoded_message

    def decode(self, encoded_message):
        decoded_bytes = base64.b64decode(encoded_message.encode('utf-8'))
        decoded_message = decoded_bytes.decode('utf-8')
        return decoded_message
