import string
def nice_strings(fname):
    n = 1
    for line in open(fname):
        rule_1 = False
        rule_2 = False
        line = line.strip()
        for s1 in string.ascii_lowercase:
            for s2 in string.ascii_lowercase:
                s = s1 + s2 
                if line.count(s) == 2:
                    rule_1 = True

        for idx, char in enumerate(line):
            if idx == len(line) - 2:
                break 
            if line[idx] == line[idx + 2] and line[idx + 1] != line[idx]:
                rule_2 = True
        if rule_1 and rule_2:
            n += 1
    return n




if __name__ == "__main__":
    print(nice_strings('input.txt'))