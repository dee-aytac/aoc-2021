def hex_to_bin(n):
    if n == "0":
        return "0000"
    elif n == "1":
        return "0001"
    elif n == "2":
        return "0010"
    elif n == "3":
        return "0011"
    elif n == "4":
        return "0100"
    elif n == "5":
        return "0101"
    elif n == "6":
        return "0110"
    elif n == "7":
        return "0111"
    elif n == "8":
        return "1000"
    elif n == "9":
        return "1001"
    elif n == "A":
        return "1010"
    elif n == "B":
        return "1011"
    elif n == "C":
        return "1100"
    elif n == "D":
        return "1101"
    elif n == "E":
        return "1110"
    elif n == "F":
        return "1111"


def parse(buffer, sum_=0):
    n = 0
    try:
        ver_no, id_ = int(buffer[:n + 3], 2), int(buffer[n + 3:n + 6], 2)
    except:
        return sum_
    n += 6
    #print("Added", ver_no, "to sum")
    sum_ += ver_no
    if id_ == 4:
        finish = False
        while not finish:
                if buffer[n] == "0":
                    finish = True
                n += 5
        return parse(buffer[n:], sum_)

    else:
        try:
            length_id = int(buffer[n])
        except:
            return sum_
        n += 1
        if length_id == 0:
            try:
                length_of_subpackages = int(buffer[n:n + 15], 2)
            except:
                return sum_
            n += 15
            return parse(buffer[n:n+length_of_subpackages], sum_) + parse(buffer[n+length_of_subpackages:])
        elif length_id == 1:
            num_of_subpackages = int(buffer[n:n + 11], 2)
            n += 11
            return  parse(buffer[n:], sum_)
    return sum_
         
for line in open('input.txt'):
    text_ = ""
    for char in line:
        text_ += hex_to_bin(char)
    x = parse(text_, 0)
    print(x)
