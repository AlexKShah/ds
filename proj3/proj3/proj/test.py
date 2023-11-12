import unittest
from proj.mystack import MyPriorityQueue, HuffmanNode


def build_huffman_tree(frequency_table):
    priority_queue = MyPriorityQueue()
    for char, freq in frequency_table.items():
        priority_queue.push(HuffmanNode(char, freq))

    while priority_queue.size() > 1:
        left = priority_queue.pop()
        right = priority_queue.pop()
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        priority_queue.push(merged)

    return priority_queue.pop()


def generate_codes(node, prefix="", code_map={}):
    if node is None:
        return

    if node.char is not None:
        code_map[node.char] = prefix

    generate_codes(node.left, prefix + "0", code_map)
    generate_codes(node.right, prefix + "1", code_map)
    return code_map


def encode_text(text, code_map):
    return ''.join(code_map.get(char, '') for char in text)


def decode_text(encoded_text, decoding_map):
    decoded_text = ''
    current_code = ''
    for bit in encoded_text:
        current_code += bit
        if current_code in decoding_map:
            decoded_text += decoding_map[current_code]
            current_code = ''
    return decoded_text


# Frequency table (Ensure this is consistent with the text to be encoded)
frequency_table = {
    "A": 19, "B": 16, "C": 17, "D": 11, "E": 42, "F": 12, "G": 14,
    "H": 17, "I": 16, "J": 5, "K": 10, "L": 20, "M": 19, "N": 24,
    "O": 18, "P": 13, "Q": 1, "R": 25, "S": 35, "T": 25, "U": 15,
    "V": 5, "W": 21, "X": 2, "Y": 8, "Z": 3
}

# Build Huffman Tree and generate codes
huffman_root = build_huffman_tree(frequency_table)
huffman_codes = generate_codes(huffman_root)

# Reverse the Huffman codes for decoding
huffman_decoding_map = {v: k for k, v in huffman_codes.items()}

# Encode and Decode "Hello World"
original_text = "Hello World".upper()
original_encoded = "1101101000010001111100011111101000000101100"
encoded_text = encode_text(original_text, huffman_codes)
decoded_text = decode_text(original_encoded, huffman_decoding_map)

print("Original Text:\t", original_text)
print("Encoded Text:\t", encoded_text)
print("Expected:\t\t " + original_encoded)
print("Decoded Text:\t", decoded_text)
print("Expected:\t\t " + original_text)
