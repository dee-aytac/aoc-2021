import re

def decompress(text):
    regex = re.compile(r'\((\d+)x(\d+)\)')
    output = regex.search(text)
    if output == None:
        return len(text)
    start = output.start()
    length, repeat = int(output.group(1)), int(output.group(2))
    new_start =  output.start() + len(output.group())
    # print(f"Found {output}.Start is {start} New start is {new_start}. Length: {length} Repeat: {repeat}")
    nested_length = decompress(text[new_start:new_start+length])
    return len(text[:start]) + nested_length * repeat + decompress(text[new_start + length:])

def solution(fname):
    with open(fname, 'r') as f:
            content = f.read().strip().split('\n')[0]
    return decompress(content)

if __name__ == "__main__":
    print(solution("input.txt"))