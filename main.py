from AlphabetGenerator import AlphabetGenerator
from Base64Cipher import Base64Cipher
from CaesarCipher import CaesarCipher
from ReverseCipher import ReverseCipher
from Huffman import encode_message, decode_message, HuffmanTree, HuffmanCoding

if __name__ == '__main__':
    # Пример использования программы
    start_char = 'a'
    end_char = 'z'
    generator = AlphabetGenerator(start_char, end_char)
    alphabet = generator.generate_alphabet()

    caesar_cipher = CaesarCipher(3, alphabet)
    reverse_cipher = ReverseCipher()
    base64_cipher = Base64Cipher()

    message = "hello misis!"

    encoded_message_caesar = caesar_cipher.encode(message)
    decoded_message_caesar = caesar_cipher.decode(encoded_message_caesar)

    encoded_message_reverse = reverse_cipher.encode(message)
    decoded_message_reverse = reverse_cipher.decode(encoded_message_reverse)

    encoded_message_base64 = base64_cipher.encode(message)
    decoded_message_base64 = base64_cipher.decode(encoded_message_base64)

    print("Исходное сообщение:", message)
    print("Закодированное сообщение (шифр Цезаря):", encoded_message_caesar)
    print("Декодированное сообщение (шифр Цезаря):", decoded_message_caesar)
    print("Закодированное сообщение (обратный шифр):", encoded_message_reverse)
    print("Декодированное сообщение (обратный шифр):", decoded_message_reverse)
    print("Закодированное сообщение (Base64):", encoded_message_base64)
    print("Декодированное сообщение (Base64):", decoded_message_base64)

    # Строим дерево Хаффмана
    huffman_tree = HuffmanTree(message)

    # Получаем коды Хаффмана
    huffman_coding = HuffmanCoding(huffman_tree)

    print(f"Huffman Codes: {huffman_coding.codes}")

    # Кодируем сообщение
    encoded_message = encode_message(message, huffman_coding.codes)
    print(f"Encoded message: {encoded_message}")

    # Декодируем сообщение
    decoded_message = decode_message(encoded_message, huffman_coding.codes)
    print(f"Decoded message: {decoded_message}")
