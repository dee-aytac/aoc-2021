def calculate_paper(fname):
    total = 0
    for line in open(fname, 'r'):
        l, w, h = line.strip().split('x')
        l, w, h = int(l), int(w), int(h)
        lst = [l, w, h]
        if line:
            # l, w, h
            # 2*l*w + 2*w*h + 2*h*l]
            total += (2 * l * w + 2 * w * h + 2 * h * l) + sorted(lst)[0] * sorted(lst)[1]
    return total



if __name__ == "__main__":
    print(calculate_paper('input.txt'))