from collections import defaultdict

def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().split('\n')
    stacks = defaultdict(list)
    build_part, move_part = content[0 : content.index("") - 1], content[content.index("") + 1:]
    for line in reversed(build_part):
        for idx in range(0, len(line), 4):
            if line[idx] == "[":
                dict_key = str(int(idx // 4) + 1)
                stacks[dict_key].append(line[idx + 1])
    for line in move_part:
        number, from_, to_ = line.split(" ")[1], line.split(" ")[3], line.split(" ")[5]
        for _ in range(int(number)):
            stacks[to_].append(stacks[from_].pop())
    top_stacks = ""
    for key in sorted(stacks.keys()):
        top_stacks += stacks[key].pop()
    return top_stacks


if __name__ == "__main__":
    print(solution('input.txt')) 
