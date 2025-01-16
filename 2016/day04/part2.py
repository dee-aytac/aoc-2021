import collections

def encrypt(text,s):
    result = ""
    for char in text:
        if char == "-":
            result += " "
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result

def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    total_sum = 0
    for line in content:
        letters, listed = line.split('[')
        letters = letters.split('-')
        sector_id = letters[-1]
        letters = letters[:-1]
        str_letters = ""
        for part in letters:
            str_letters += part + "-"
        encrypted = encrypt(str_letters, int(sector_id))
        if "north" in encrypted:
            print(encrypted)
            return sector_id
            
if __name__ == "__main__":
    print(solution('input.txt'))