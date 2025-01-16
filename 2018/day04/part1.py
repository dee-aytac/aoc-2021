from collections import Counter

def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    day = 1
    content.sort()
    guard_id = -1
    guard_sleep_schedule = dict()
    idx = 0
    while idx < len(content) - 2:
        if "Guard" in content[idx + 1]:
            idx += 1
            continue
        curr = content[idx]
        if "Guard" in curr:
            date, info = curr.split('] ')
            date = date[1:]
            guard_id = info.split(' ')[1][1:]
        else:
            idx -= 1
        falls_asleep_hour = content[idx + 1].split(' ')[1][:-1]
        wake_up_hour = content[idx + 2].split(' ')[1][:-1]
        for minute in range(int(falls_asleep_hour.split(':')[1]), int(wake_up_hour.split(':')[1])):
            if guard_id not in guard_sleep_schedule.keys():
                guard_sleep_schedule[guard_id] = list()
            guard_sleep_schedule[guard_id].append(minute)
        idx += 3
    longest_sleep = -1
    longest_sleeper = -1
    for key in guard_sleep_schedule.keys():
        if len(guard_sleep_schedule[key]) > longest_sleep:
            longest_sleeper = key
            longest_sleep = len(guard_sleep_schedule[key])

    common_val = Counter(guard_sleep_schedule[longest_sleeper]).most_common(1)[0][0]
    return common_val * int(longest_sleeper)

if __name__ == "__main__":
    print(solution('input.txt')) 

