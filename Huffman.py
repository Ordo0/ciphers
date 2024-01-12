from heapq import heappush, heappop, heapify
from collections import defaultdict


class Node:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right


class HuffmanTree:
    def __init__(self, message):
        self.frequency = self.calculate_frequency(message)
        self.root = self.build_tree()

    def calculate_frequency(self, message):
        frequency = defaultdict(int)
        for char in message:
            frequency[char] += 1
        return frequency

    def build_tree(self):
        priority_queue = []
        counter = 0
        for char, freq in self.frequency.items():
            heappush(priority_queue, (freq, counter, Node(char, freq)))
            counter += 1

        while len(priority_queue) > 1:
            freq1, _, node1 = heappop(priority_queue)
            freq2, _, node2 = heappop(priority_queue)
            heappush(priority_queue, (freq1 + freq2, counter, Node(None, freq1 + freq2, node1, node2)))
            counter += 1
        return priority_queue[0][2]


class BuilderCodes:
    def build_codes(self, node, code, codes) -> None:
        if node.char is not None:
            codes[node.char] = code
        else:
            self.build_codes(node.left, code + '0', codes)
            self.build_codes(node.right, code + '1', codes)


class HuffmanCoding(BuilderCodes):
    def __init__(self, huffman_tree):
        self.tree = huffman_tree
        self.codes = self.get_codes()

    def get_codes(self):
        codes = {}
        self.build_codes(self.tree.root, '', codes)
        return codes


def encode_message(message, codes):
    encoded_message = ''
    for char in message:
        encoded_message += codes[char]
    return encoded_message


def decode_message(encoded_message, codes):
    reversed_codes = {v: k for k, v in codes.items()}
    decoded_message = ''
    code = ''
    for bit in encoded_message:
        code += bit
        if code in reversed_codes:
            decoded_message += reversed_codes[code]
            code = ''
    return decoded_message
