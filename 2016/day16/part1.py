
def dragon_curve(inp, length):
    a = inp
    while True:
        b = a
        b = b[::-1]
        new_b = ""
        for char in b:
            if char == "0":
                new_b += "1"
            else:
                new_b += "0"
        result = a + "0" + new_b
        if len(result) >= length:
            return result
        a = result

def solution(content, length):
    disk =  dragon_curve(content, length)
    if len(disk) >= length:
        disk = disk[:length]
    pair_length = 2
    pairs = [disk[i:i+pair_length] for i in range(0, len(disk), pair_length)]
    while True:
        checksum = ""
        for pair in pairs:
            if pair[0] == pair[1]:
                checksum += "1"
            else:
                checksum += "0"
        if len(checksum) % 2 == 1:
            return checksum
        pairs = [checksum[i:i+pair_length] for i in range(0, len(checksum), pair_length)]

if __name__ == "__main__":
    print(solution('00111101111101000', 272))