#0 - abcef
#1 - cf
#2 - acdeg
#3 - acdfg
#4 - bcdf
#5 - abdfg
#6 - abdefg
#7 - acf
#8 - abcdefg
#9 - abcdfg

def return_digit(s):
    if len(s) == 2:
        return 1
    elif len(s) == 3:
        return 7
    elif len(s) == 4:
        return 4
    elif len(s) == 7:
        return 8
    

with open('input.txt', 'r') as f:
    lines = f.readlines()
    repeats = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9:0}
    for line in lines:
        l = line.replace('\n', '').split('|')
        part_1 = l[0].split(' ')
        part_2 = l[1].split(' ')
        for n in part_2:
            d = return_digit(n)
            if d:
                repeats[d] += 1
print(repeats[1] + repeats[4] + repeats[7] + repeats[8])