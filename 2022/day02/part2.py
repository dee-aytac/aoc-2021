
def evaluate(elf_move, outcome):
    points = {"rock": 1, "paper": 2, "scissors": 3}
    # first element: will wins against, second element: will lose against
    compare = {
            "rock": ["scissors", "paper"],
            "paper": ["rock", "scissors"],
            "scissors": ["paper", "rock"], 
    }
    if outcome == "Y":
        return 3 + points[elf_move]
    elif outcome == "Z":
        return 6 + points[compare[elf_move][1]]
    else:
        return 0 + points[compare[elf_move][0]]

def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    total_points = 0
    for line in content:
        elf, outcome = line.split(' ')
        elf_move = "rock" if elf == "A" else ("paper" if elf == "B" else "scissors")
        total_points += evaluate(elf_move, outcome)
    return total_points

if __name__ == "__main__":
    print(solution('input.txt')) 