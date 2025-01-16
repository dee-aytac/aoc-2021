def find_encoded(fname):
    l0 = 0
    l1 = 0
    x = 0
    y = 0
    for line in open(fname):
        hex_c = 0 # hex count
        sl_c = 0 # backslash count 
        d_sl_c = 0 # double backslash count
        l0 = 0 # local chars
        l1 = 0 # local memory
        l0 = len(line.strip())
        real = line.strip()[1:-1]
        
        if real:
            sl_c = real.count('\\')
            if sl_c:
                l1 = l0 + 4 + sl_c * 2
                if real[0] == "\\":
                    l1 = l0 + 1

            else:
                l1 = l0 + 3
        else:
            l1 = l0 + 4
        x += l0 
        y += l1
        print(l1, line.strip())
    return (y-x) 

if __name__ == "__main__":
    print(find_encoded("input.txt"))