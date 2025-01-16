
def solution(fname, width, height):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')[0]
    layer_idx = 1
    layers = dict()
    total_zeros = float('inf')
    product = 0
    for idx in range(0, len(content), width*height):
        line = content[idx:idx+width*height]
        layers[layer_idx] = [int(char) for char in line]
        if layers[layer_idx].count(0) < total_zeros:
            total_zeros = layers[layer_idx].count(0)
            product = layers[layer_idx].count(1) * layers[layer_idx].count(2)
        layer_idx += 1
    return product
if __name__ == "__main__":
    print(solution('input.txt', 25, 6)) 
