"""
This program receives a frequency table, and encoded or cleartext text to be used in huffman coding scheme

__author__ = Alex Shah
__version__ = proj3
"""


# from proj.mystack import MyPriorityQueue, HuffmanNode
# test_case(huffman_codes, huffman_root)
def test_case(huffman_codes, huffman_root):
    # DEBUG
    # given_codes = {
    #     'E': '010',
    #     'S': '1110',
    #     'T': '1001',
    #     'R': '1000',
    #     'N': '0111',
    #     'W': '0011',
    #     'L': '0010',
    #     'A': '11111',
    #     'M': '0000',
    #     'O': '11110',
    #     'H': '11011',
    #     'C': '11010',
    #     'I': '11001',
    #     'B': '11000',
    #     'U': '10111',
    #     'G': '10110',
    #     'P': '10100',
    #     'F': '01101',
    #     'D': '01100',
    #     'K': '00011',
    #     'Y': '101011',
    #     'V': '000101',
    #     'J': '000100',
    #     'Z': '1010101',
    #     'X': '10101001',
    #     'Q': '10101000'
    # }
    #
    # print("Comparing generated Huffman codes with given codes...")
    # for char, given_code in given_codes.items():
    #     generated_code = huffman_codes.get(char)
    #     if generated_code != given_code:
    #         print(f"Mismatch for '{char}': Generated Code: {generated_code}, Given Code: {given_code}")
    #     else:
    #         print(f"Match for '{char}': Code: {generated_code}")

    # Encode and Decode "Hello World" to test functionality
    original_text = "Hello World".upper()
    original_encoded = "1101101000010001111100011111101000000101100"
    encoded_text = huffman_encoding(original_text, huffman_codes)
    decoded_text = huffman_decoding(original_encoded, huffman_root)

    print("Original Text:\t", original_text)
    print("Encoded Text:\t", encoded_text)
    print("Expected:\t\t " + original_encoded)
    print("Decoded Text:\t", decoded_text)
    print("Expected:\t\t " + original_text)


def huffman_process_files(freq_file, input_file, output_file, mode):
    frequency_table = {}
    for line in freq_file:
        char, freq = line.strip().split(' - ')
        frequency_table[char] = int(freq)

    huffman_root = build_huffman_tree(frequency_table)
    huffman_codes = generate_codes(huffman_root)

    if mode == 'encode':
        for line in input_file:
            encoded_line = huffman_encoding(line.strip(), huffman_codes)
            output_file.write(encoded_line + "\n")
    elif mode == 'decode':
        for encoded_line in input_file:
            decoded_text = huffman_decoding(encoded_line.strip(), huffman_root)
            output_file.write(decoded_text + "\n")
    # DEBUG
    test_case(huffman_codes, huffman_root)


class MyPriorityQueue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        # Sort by frequency, then single-letter precedence, then alphabetically
        self.items.sort(key=lambda x: (x.freq, len(x.char) if x.char else 0, x.char if x.char else ""))

    def pop(self):
        return self.items.pop(0) if self.items else None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None


def build_huffman_tree(frequency_table):
    priority_queue = MyPriorityQueue()
    for char, freq in frequency_table.items():
        priority_queue.push(HuffmanNode(char.upper(), freq))  # Consistent upper case

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
        return code_map

    if node.char is not None:
        code_map[node.char] = prefix

    generate_codes(node.left, prefix + "0", code_map)
    generate_codes(node.right, prefix + "1", code_map)

    return code_map


def huffman_encoding(text, code_map):
    encoded_text = []
    for char in text.upper():
        if char in code_map:
            encoded_char = code_map[char]
            encoded_text.append(encoded_char)
    final_encoded_string = ''.join(encoded_text)
    #print(f"Final Encoded String: {final_encoded_string}")
    return final_encoded_string


def huffman_decoding(encoded_text, root):
    decoded_text = ""
    current_node = root
    for bit in encoded_text:
        if bit == '0':
            current_node = current_node.left
        elif bit == '1':
            current_node = current_node.right

        if current_node is None:
            raise ValueError("Invalid encoded sequence encountered at bit: " + bit)

        if current_node.char:
            decoded_text += current_node.char
            current_node = root  # Reset to root after reaching a leaf node
    return decoded_text
