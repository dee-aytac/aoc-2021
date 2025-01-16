#0 - abcefg
#1 - cf
#2 - acdeg
#3 - acdfg
#4 - bcdf
#5 - abdfg
#6 - abdefg
#7 - acf
#8 - abcdefg
#9 - abcdfg

# Used the scheme.png to differentiate segments

from itertools import combinations


def return_digit(s, mapping): 
    encoded = "".join(sorted(s))
    if len(s) == 2:
        return 1
    elif len(s) == 3:
        return 7
    elif len(s) == 4:
        return 4
    elif len(s) == 5:
        if mapping[0][0] in encoded and mapping[0][1] in encoded:
            return 3
        else:
            comb = combinations(mapping[4], 3)
            for i in list(comb):
                if i[0] in encoded and i[1] in encoded and i[2] in encoded:
                    return 5
            return 2

    elif len(s) == 6:
        if mapping[4][0] in encoded and mapping[4][1] in encoded and mapping[4][2] in encoded and mapping[4][3] in encoded:
            return 9
        elif mapping[7][0] in encoded and mapping[7][1] in encoded and mapping[7][2] in encoded :
            return 0
        else:
            return 6

    elif len(s) == 7:
        return 8


with open('input.txt', 'r') as f:
    lines = f.readlines()
    output = 0
    for line in lines:
        f_ = line.replace('\n', '').split('|')
        x = f_[0].split(' ')
        y = f_[1].split(' ')
        q = ""
        mapping = {0: "", 7: "", 4: ""}
        for n in x:
            if len(n) == 2:
                mapping[0] = n 
            elif len(n) == 3:
                mapping[7] = n
            elif len(n) == 4:
                mapping[4] = n
        for n in y:
            if len(n):
                d = return_digit(n, mapping)
                q += str(d)
        output += int(q)
    print(output)
 
