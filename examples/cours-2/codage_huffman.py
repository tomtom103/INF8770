class Node:
    def __init__(self, prob, symbol, left=None, right=None):
        self.prob = prob
        self.symbol = symbol
        self.left = left
        self.right = right
        self.code = ''

def calculate_probability(data: str):
    symbols = {}
    for element in data:
        if element in symbols:
            symbols[element] += 1
        else:
            symbols[element] = 1
    return symbols

codes = {}

def calculate_codes(node: Node, val=''):
    newVal = val + str(node.code)

    if node.left:
        calculate_codes(node.left, newVal)
    if node.right:
        calculate_codes(node.right, newVal)
    
    if not node.left and not node.right:
        codes[node.symbol] = newVal
    return codes

def output_encoded(data: str, coding: dict):
    encoded_output = []
    for c in data:
        # print(coding[c], end = '')
        encoded_output.append(coding[c])
    return ''.join([str(item) for item in encoded_output])

def total_gain(data: str, coding: dict):
    before_compression = len(data) * 8
    after_compression = 0
    symbols = coding.keys()
    for symbol in symbols:
        count = data.count(symbol)
        after_compression += count * len(coding[symbol])

    print("Space usage before compression (in bits): ", before_compression)
    print("Space usage after compression (in bits): ", after_compression)

if __name__ == "__main__":
    data = "AAAABAAAAAABBBAABAAAACABBABCDAADACAAAAAAAAAAAAAAAAAAAAAABABABBBA"
    print("Original message: ", data)
    symbol_with_probs = calculate_probability(data)
    symbols = symbol_with_probs.keys()
    probabilities = symbol_with_probs.values()

    print("Symbols: ", symbols)
    print("Probabilities: ", probabilities)

    nodes = []

    for symbol in symbols:
        nodes.append(Node(symbol_with_probs.get(symbol), symbol))
    
    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.prob)

        right: Node = nodes[0]
        left: Node = nodes[1]

        left.code = 0
        right.code = 1

        newNode = Node(left.prob + right.prob, left.symbol + right.symbol, left, right)

        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)

    huffman_encoding = calculate_codes(nodes[0])
    print(f"Huffman encoding: {huffman_encoding}", end='\n')
    total_gain(data, huffman_encoding)
    print(f"Encoded output: {output_encoded(data, huffman_encoding)}")
