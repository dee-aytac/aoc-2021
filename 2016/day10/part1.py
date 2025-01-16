
def add_to_dict(dictionary, key, value):
    if key in dictionary.keys():
        dictionary[key].append(value)
        dictionary[key].sort()
    else:
        dictionary[key] = [value]

def solution(fname, val1, val2):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    remaining_lines = content
    values = dict()
    while True:
        if len(remaining_lines) == 0:
            break
        length_lines = len(remaining_lines)
        to_remove = set()
        for idx in range(length_lines):
            line = remaining_lines[idx]
            args = line.split(' ')
            if args[0] == "value":
                value = int(args[1])
                dest = args[-1]
                add_to_dict(values, dest, value)
                to_remove.add(idx)
            elif args[0] == "bot":
                pass
                src = args[1]
                dest_low, dest_high = args[6], args[11]
                if src in values.keys() and len(values[src]) == 2:
                    if val1 in values[src] and val2 in values[src]:
                        return src
                    add_to_dict(values, dest_low, values[src][0])
                    add_to_dict(values, dest_high, values[src][1])
                    to_remove.add(idx)
                    del values[src]
            else:
                print("unknown command")
        for index in sorted(to_remove, reverse=True):
            del remaining_lines[index]
    return values

if __name__ == "__main__":
    print(solution('input.txt', 61, 17))