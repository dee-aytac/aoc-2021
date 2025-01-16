import json

def find_sum_list(data):
    local_sum = 0
    for i in data:
        if isinstance(i, dict):
            local_sum += find_sum_dict(i)
        if isinstance(i, list):
            local_sum += find_sum_list(i)
        elif isinstance(i, int):
            local_sum += i
    return local_sum

def find_sum_dict(data):
    total_sum = 0 
    if "red" in data.values():
        return 0
    for key, value in data.items():
        if isinstance(value, dict):
            total_sum += find_sum_dict(value)
        if isinstance(value, list):
            total_sum += find_sum_list(value)
        elif isinstance(value, int):
            total_sum += value
    return total_sum


if __name__ == "__main__":
    with open("input.txt") as f:
        content = f.read()
    data = json.loads(content)
    print(find_sum_dict(data))