
def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')[0]
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
            break
        content = new_content

    return len(content)

if __name__ == "__main__":
    print(solution('input.txt')) 