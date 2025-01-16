
# 0 is black, 1 is white, and 2 is transparent.
def solution(fname, width, height):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')[0]
    layer_idx = 1
    layers = dict()
    for idx in range(0, len(content), width*height):
        line = content[idx:idx+width*height]
        layers[layer_idx] = [char for char in line]
        layer_idx += 1
    final_image = list()
    x_pos, y_pos = 0, 0
    while x_pos < height:
        decoded_line = ""
        while y_pos < width:
            for key in layers.keys():
                char = layers[key][y_pos + (x_pos) * width]
                if char == "0":
                    decoded_line += "."
                    break
                if char == "1":
                    decoded_line += "#"
                    break
                else:
                    continue
            y_pos += 1
        final_image.append(decoded_line)
        y_pos = 0
        x_pos += 1
    for row in final_image:
        print(row)

if __name__ == "__main__":
    solution('input.txt', 25, 6)
