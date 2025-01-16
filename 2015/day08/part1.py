def find_memory(fname):
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
            hex_c = real.count("\\x")
            sl_c = real.count("\\")
            d_sl_c = real.count(r"\\")
            error = real.count(r"\\x")
            if hex_c != 0:
                if sl_c > hex_c:
                    l1 = len(real) - (hex_c * 3) - ((sl_c - hex_c) * 1)
                    if d_sl_c > 0:
                        l1 += d_sl_c
                else:
                    l1 = len(real) - (hex_c * 3) 
                if error:
                    l1 += 1
            else:
                if sl_c:
                    l1 = len(real) - (sl_c)
                    if d_sl_c > 0:
                        l1 += d_sl_c
                else:
                    l1 = len(real)
        x += l0 
        y += l1
    return x - y

if __name__ == "__main__":
    print(find_memory("input.txt"))