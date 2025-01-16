import hashlib
def find_min(key):
    for i in range(100000000):
        txt = key + str(i)
        result =  hashlib.md5(txt.encode())
        if result.hexdigest()[:5] == "00000":
            return i
    return None


if __name__ == "__main__":
    print(find_min("iwrupvqb"))