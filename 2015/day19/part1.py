
def solution(fname):
    with open(fname, 'r') as f:
        lines = f.read().splitlines() 
    inp = lines[-1]
    translations = list()
    for line in lines:
        if len(line.split(" => ")) == 2: 
            x, y = line.split(" => ")[0], line.split(" => ")[1]
            translations.append([x, y])
    distinct_molecules = set()
    rep = 0
    last_char = "-"
    for pos, char in enumerate(inp):
        for x, translation in translations:
            if x == char:
                rep += 1
                new_molecule = inp[:pos] + translation + inp[pos+1:]
                # print(f"New molecule: {new_molecule} | Replaced {x} with {translation}")
                distinct_molecules.add(new_molecule)

            elif  x == (last_char+char):
                rep += 1
                new_molecule = inp[:pos-1] + translation + inp[pos+1:]
                # print(f"New molecule: {new_molecule} | Replaced {x} with {translation}")
                distinct_molecules.add(new_molecule)
        last_char = char
    return f"{len(distinct_molecules)} distinct molecules over {rep} replacements"
    
if __name__ == "__main__":
    print(solution("input.txt"))