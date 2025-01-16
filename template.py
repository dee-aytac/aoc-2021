
def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    for line in content:
        pass
if __name__ == "__main__":
    print(solution('input.txt')) 
