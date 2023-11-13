# real freq
frequency_table = {'A': 19,
                   'B': 16,
                   'C': 17,
                   'D': 11,
                   'E': 42,
                   'F': 12,
                   'G': 14,
                   'H': 17,
                   'I': 16,
                   'J': 5,
                   'K': 10,
                   'L': 20,
                   'M': 19,
                   'N': 24,
                   'O': 18,
                   'P': 13,
                   'Q': 1,
                   'R': 25,
                   'S': 35,
                   'T': 25,
                   'U': 15,
                   'V': 5,
                   'W': 21,
                   'X': 2,
                   'Y': 8,
                   'Z': 3
                   }
import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def is_leaf(self):
        return self.left is None and self.right is None

    def __lt__(self, other):
        # Tie-breaking rule: single-letter groups have precedence
        if self.freq == other.freq:
            if self.is_leaf() and other.is_leaf():
                return self.char < other.char  # Alphabetically
            return self.is_leaf()  # Single letter groups first
        return self.freq < other.freq

def build_huffman_tree(frequency_table):
    priority_queue = [Node(char, freq) for char, freq in frequency_table.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(priority_queue, merged)

    return priority_queue[0] if priority_queue else None

def assign_codes_preorder(node, code, codes):
    if node is not None:
        if node.char is not None:
            codes[node.char] = code
        assign_codes_preorder(node.left, code + "0", codes)
        assign_codes_preorder(node.right, code + "1", codes)

def get_huffman_codes(root):
    codes = {}
    assign_codes_preorder(root, "", codes)
    return codes

# Example usage
root = build_huffman_tree(frequency_table)
codes = get_huffman_codes(root)

for char, code in sorted(codes.items()):
    print(f"{char}: {code}")
