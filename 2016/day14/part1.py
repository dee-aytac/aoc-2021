import hashlib

def solution(content):
    salt = content
    total_keys = 0
    idx = 0
    to_look_for = dict()
    indexes = dict()
    count = dict()
    while True:
        add = False
        string = salt + str(idx)
        result = hashlib.md5(string.encode()).hexdigest()
        found = False
        for i in range(len(result) - 2):
            if found:
                break
            if result[i:i+3] == result[i] * 3:
                for local_idx in range(idx, idx + 1000):
                    if found:
                        break
                    string = salt + str(local_idx)
                    new_result = hashlib.md5(string.encode()).hexdigest()
                    if result[i] * 5 in new_result:
                        total_keys += 1
                        found = True
        #     if found == True:
        #         break
        #     if result[i:i+3] == result[i] * 3:
        #         add = True
        #         to_add = result[i] * 5
        #         #print(result, idx, "looking for", to_add)
        #         #found = True   
        # for key in list(to_look_for):
        #     if key in result:
        #         total_keys += count[key]
        #         if total_keys >= 64:
        #             return indexes[key]
        #     to_look_for[key] -= 1
        #     if to_look_for[key] <= 0:
        #         del to_look_for[key]
        #         count[key] -= 1
        # if add:
        #     print("adding", to_add)
        #     if to_add in to_look_for:
        #         count[to_add] += 1
        #     else:
        #         count[to_add] = 0
        #     to_look_for[to_add] = 1000
        #     indexes[to_add] = idx
        if total_keys > 64:
            return idx
        idx += 1

if __name__ == "__main__":
    print(solution('abc'))