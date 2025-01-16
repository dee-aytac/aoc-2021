import random

def solution(fname):
    with open(fname, 'r') as f:
        lines = f.read().splitlines() 
    inp = lines[-1]
    translations = list()
    possible_molecules = set()
    for line in lines:
        if len(line.split(" => ")) == 2: 
            generator, generated = line.split(" => ")[0], line.split(" => ")[1]
            possible_molecules.add(generated)
            translations.append((generator, generated))
    answer = 0
    current_molecule = inp
    while len(current_molecule) > 1:
        guess_molecule = current_molecule
        for base, goal in translations:
            while goal in current_molecule:
                answer += current_molecule.count(goal)
                current_molecule = current_molecule.replace(goal, base)
            if guess_molecule == current_molecule:
                answer = 0
                current_molecule = inp
                random.shuffle(translations)
                
    return answer

if __name__ == "__main__":
    print(solution("input.txt"))