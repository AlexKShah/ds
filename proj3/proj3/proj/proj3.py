"""
This program receives a frequency table, and encoded or cleartext text to be used in huffman coding scheme

__author__ = Alex Shah
__version__ = proj3
"""

from proj.mystack import MyPriorityQueue, HuffmanNode


def test_case(huffman_codes, huffman_root, output_file):
    # Encode and Decode "Hello World" to test functionality
    original_text = "Hello World".upper()
    original_encoded = "1101101000010001111100011111101000000101100"
    encoded_text = huffman_encoding(original_text, huffman_codes, output_file)
    decoded_text = huffman_decoding(original_encoded, huffman_root, output_file)

    print("Original Text:\t", original_text)
    print("Encoded Text:\t", encoded_text[0])
    print("Expected Enc:\t " + original_encoded)
    print("Decoded Text:\t", decoded_text)
    print("Expected Dec:\t " + original_text.replace(" ", ""))


def huffman_process_files(freq_file, encoded_file, clear_file, output_file):
    """
    :param freq_file: frequency table file
    :param encoded_file: file to decode
    :param clear_file: file to encode
    :param output_file: file to write to
    """
    frequency_table = build_frequency_table(freq_file)
    huffman_root = build_huffman_tree(frequency_table)
    huffman_codes = get_huffman_codes(huffman_root)

    output_file.write("####Encoded Lines:\n\n")
    for idx, clear_line in enumerate(clear_file):
        encoded_line, skipped_chars = huffman_encoding(clear_line.strip(), huffman_codes, output_file)
        output_file.write("Original #" + str(idx) + ": \t" + clear_line)
        if skipped_chars:
            output_file.write("Skipped characters during encoding: " + ", ".join(skipped_chars) + "\n")
        output_file.write("Encoded: \t\t" + encoded_line + "\n")
        output_file.write("Re-Decoded: \t" + huffman_decoding(encoded_line, huffman_root, output_file) + "\n\n")

    output_file.write("\n\n####Decoded Lines:\n\n")
    for idx, encoded_line in enumerate(encoded_file):
        decoded_text = huffman_decoding(encoded_line.strip(), huffman_root, output_file)
        output_file.write("Original #" + str(idx) + "\t" + encoded_line)
        output_file.write("Decoded: \t\t" + decoded_text + "\n")
        output_file.write("Re-Encoded: \t" + huffman_encoding(decoded_text, huffman_codes, output_file)[0] + "\n\n")

    # DEBUG
    test_case(huffman_codes, huffman_root, output_file)


def build_frequency_table(freq_file):
    frequency_table = {}
    for line in freq_file:
        char, freq = line.strip().split(' - ')
        frequency_table[char] = int(freq)
    return frequency_table


def build_huffman_tree(frequency_table):
    priority_queue = MyPriorityQueue()
    # push items to queue
    for char, freq in frequency_table.items():
        priority_queue.push(HuffmanNode(char, freq))

    # assign left/right
    while len(priority_queue) > 1:
        left = priority_queue.pop()
        right = priority_queue.pop()

        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        priority_queue.push(merged)

    return priority_queue.pop()


def get_huffman_codes(root):
    codes = {}
    assign_codes_preorder(root, "", codes)
    return codes


def assign_codes_preorder(node, code, codes):
    if node is not None:
        if node.char is not None:
            codes[node.char] = code
        # Use recursion to build codes in preorder
        assign_codes_preorder(node.left, code + "0", codes)
        assign_codes_preorder(node.right, code + "1", codes)


def huffman_encoding(text, code_map, output_file):
    encoded_text = []
    skipped_chars = []

    for char in text.upper():
        if char in code_map:
            encoded_char = code_map[char]
            encoded_text.append(encoded_char)
        else:
            skipped_chars.append(char)

    final_encoded_string = ''.join(encoded_text)

    # if skipped_chars:
    #    output_file.write("Skipped characters during encoding: " + ", ".join(skipped_chars) + "\n")

    return final_encoded_string, skipped_chars


def huffman_decoding(encoded_text, root, output_file):
    decoded_text = ""
    current_node = root
    error_flag = False

    for bit in encoded_text:
        if bit == '0':
            current_node = current_node.left
        elif bit == '1':
            current_node = current_node.right
        else:
            error_flag = True
            break

        if current_node is None or (current_node.char is None and bit not in ['0', '1']):
            error_flag = True
            break

        if current_node.char:
            decoded_text += current_node.char
            current_node = root

    if error_flag:
        output_file.write("Error: Invalid encoded sequence encountered.\n")

    return decoded_text
