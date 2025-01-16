def nice_strings(fname):
    n = 0
    for line in open(fname):
        rule_1 = False
        rule_2 = False
        rule_3 = True
        line = line.strip()
        w = 0
        for s in ['a', 'e', 'i', 'o', 'u']:
            w += line.count(s)
        if w >= 3:
            rule_1 = True

        for idx, char in enumerate(line):
            #print(line.strip())
            if idx == len(line) - 1:
                break 
            if line[idx] == line[idx + 1]:
                rule_2 = True
         
        if 'ab' in line or 'cd' in line or 'pq' in line or 'xy' in line:
            rule_3 = False

        if rule_1 and rule_2 and rule_3:
            n += 1
    return n




if __name__ == "__main__":
    print(nice_strings('input.txt'))