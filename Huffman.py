from heapq import heappush, heappop, heapify
from collections import defaultdict


# Создание узла дерева
class Node:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right


# Функция для кодирования сообщения
def encode_message(message):
    # Подсчет частоты встречаемости символов в сообщении
    frequency = defaultdict(int)
    for char in message:
        frequency[char] += 1

    # Создание очереди приоритетов для узлов дерева
    priority_queue = []
    counter = 0
    for char, freq in frequency.items():
        heappush(priority_queue, (freq, counter, Node(char, freq)))
        counter += 1

    # Строим дерево Хаффмана
    while len(priority_queue) > 1:
        freq1, _, node1 = heappop(priority_queue)
        freq2, _, node2 = heappop(priority_queue)
        heappush(priority_queue, (freq1 + freq2, counter, Node(None, freq1 + freq2, node1, node2)))
        counter += 1

    # Получение кодов символов с помощью обхода дерева
    codes = {}

    def get_codes(node, code):
        if node.char is not None:
            codes[node.char] = code
        else:
            get_codes(node.left, code + '0')
            get_codes(node.right, code + '1')

    root = priority_queue[0][2]
    get_codes(root, '')

    # Кодирование сообщения
    encoded_message = ''
    for char in message:
        encoded_message += codes[char]

    return encoded_message, codes


# Функция для декодирования сообщения
def decode_message(encoded_message, codes):
    # Создание обратного словаря кодов символов
    reversed_codes = {v: k for k, v in codes.items()}

    # Декодирование сообщения
    decoded_message = ''
    code = ''
    for bit in encoded_message:
        code += bit
        if code in reversed_codes:
            decoded_message += reversed_codes[code]
            code = ''

    return decoded_message
