
def check_if_valid_triangles(sides_group): 
    valid = 0
    for i in range(3):    
        a, b, c = sides_group[0][i], sides_group[1][i], sides_group[2][i]
        print(a, b, c)
        if (a + b <= c) or (a + c <= b) or (b + c <= a) :
            pass
        else:
            valid += 1
    return valid


def get_int(variables):
    sides = list()
    for var in variables:
        try:
            sides.append(int(var))
        except:
            pass
    return sides


def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    valid_triangles = 0
    idx = 0
    while idx < len(content):
        vars1 = content[idx].split('  ')
        vars2 = content[idx+1].split('  ')
        vars3 = content[idx+2].split('  ')

        sides1 = get_int(vars1)
        sides2 = get_int(vars2)
        sides3 = get_int(vars3)
        valid_triangles += check_if_valid_triangles((sides1, sides2, sides3))
        idx += 3
    return valid_triangles

if __name__ == "__main__":
    print(solution('input.txt'))