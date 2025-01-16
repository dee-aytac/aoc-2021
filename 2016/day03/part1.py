
def check_if_valid_triangle(sides):
    a, b, c = sides[0], sides[1], sides[2]
    if (a + b <= c) or (a + c <= b) or (b + c <= a) :
        return False
    else:
        return True  

def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    valid_triangles = 0
    for line in content:
        variables = line.split('  ')
        sides = list()
        for var in variables:
            try:
                sides.append(int(var))
            except:
                pass
        print(sides, "-", check_if_valid_triangle(sides))
        if check_if_valid_triangle(sides):
            valid_triangles += 1
    return valid_triangles
    
if __name__ == "__main__":
    print(solution('input.txt'))