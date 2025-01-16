

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
#cg cbg cefg

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
        new_ = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f', 'g': 'g'}
        f_ = line.replace('\n', '').split('|')
        x = f_[0].split(' ')
        y = f_[1].split(' ')
        # for n in x:
        #     if len(n) == 2:
        #         new_[n[0]] = 'c'
        #         new_[n[1]] = 'f'
        #     elif len(n) == 3:
        #         new_[n[0]] = 'a'
        #         new_[n[1]] = 'c'
        #         new_[n[2]] = 'f'
        #     elif len(n) == 4:
        #         new_[n[0]] = 'b'
        #         new_[n[1]] = 'c'
        #         new_[n[2]] = 'd'
        #         new_[n[3]] = 'f'

        for n in y:
            d = return_digit(n)
            if d:
                print(repeats[d])
                repeats[d] += 1
            # encoded = ''.join(new_[i] for i in n)
            # print(sorted(encoded))
            # print(encoded)
print(repeats)