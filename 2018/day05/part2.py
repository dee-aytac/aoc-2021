
# be careful, might take around a minute

def solution(fname):
    with open(fname, 'r') as f:
        original_content = f.read().strip().split('\n')[0]
    all_units_in_lower = set()
    for char in original_content:
        all_units_in_lower.add(char.lower())
    
    lowest_length = float('inf')
    while len(all_units_in_lower) > 0:
        char = all_units_in_lower.pop()
        content = "".join(ch for ch in original_content if ch != char and ch != char.upper())
        print(len(all_units_in_lower), "remaining")
        while True:
            idx = 0
            length = len(content)
            new_content = ""
            while idx < length:
                curr = content[idx]
                if idx == length - 1:
                    new_content += curr
                    break
                nextt = content[idx + 1]
                if (curr.lower() == nextt.lower() 
                    and ((curr.islower() and nextt.isupper()) or (nextt.islower() and curr.isupper()))):
                    idx += 2
                else:
                    new_content += curr
                    idx += 1
            if new_content == content:
                lowest_length = min(lowest_length, len(new_content))
                break
            content = new_content

    return lowest_length

if __name__ == "__main__":
    print(solution('input.txt')) 