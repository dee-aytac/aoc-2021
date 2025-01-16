
def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    elfs = list()
    elf = 0
    for line in content:
        if line == "":
            elfs.append(elf)
            elf = 0
        else:
            elf += int(line)
    return sorted(elfs)[-1]

if __name__ == "__main__":
    print(solution('input.txt')) 
