
def evaluate(elf_move, player_move):
    points = {"rock": 1, "paper": 2, "scissors": 3}
    if elf_move == player_move:
        return 3 + points[player_move]
    elif ((player_move == "paper" and elf_move == "rock")
        or (player_move == "rock" and elf_move == "scissors")
        or (player_move == "scissors" and elf_move == "paper")):
        return 6 + points[player_move]
    else:
        return 0 + points[player_move]

def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    total_points = 0
    for line in content:
        elf, me = line.split(' ')
        elf_move = "rock" if elf == "A" else ("paper" if elf == "B" else "scissors")
        player_move = "rock" if me == "X" else ("paper" if me == "Y" else "scissors")
        total_points += evaluate(elf_move, player_move)
    return total_points

if __name__ == "__main__":
    print(solution('input.txt')) 
