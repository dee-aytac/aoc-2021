import hashlib
import collections

# gets a string and check if a char repeats length times, if does returns the char
def check_match(inp, length):
    for i in range(len(inp) - (length - 1)):
        if inp[i:i+length] == inp[i] * length:
            return inp[i]
    return None

def solution(content):
    total_keys = 0
    idx = 0
    keys = collections.defaultdict(list)
    while True:
        hash_result = content + str(idx)
        for _ in range(0, 2016 + 1):
            hash_result = hashlib.md5(hash_result.encode()).hexdigest()

        get_five = check_match(hash_result, 5)
        if get_five != None:
            for orig_idx in keys[get_five * 5]:
                if (idx - orig_idx) <= 1000:
                    print("found key", total_keys) 
                    total_keys += 1
                    if total_keys >= 64:
                        return orig_idx

        get_three = check_match(hash_result, 3)
        if get_three != None:
            keys[get_three * 5].append(idx)
        idx += 1

if __name__ == "__main__":
    print(solution('ahsbgdzn'))