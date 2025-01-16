
def solution(fname):
    with open(fname) as f:
        content = f.read().splitlines()
    reindeers = dict()
    for line in content:
        name, speed, duration, rest_time = line.split(' ')[0], line.split(' ')[3], line.split(' ')[6], line.split(' ')[13]
        reindeers[name] = {"speed": int(speed), "duration": int(duration), "rest_time": int(rest_time), "state": 0, "distance": 0, "points": 0}
    time = 0
    while time <= 2503:
        lead = float('-inf')
        for reindeer in reindeers.keys():
            if reindeers[reindeer]["state"] >= 0:
                reindeers[reindeer]["distance"] += reindeers[reindeer]["speed"]
            reindeers[reindeer]["state"] += 1
            if reindeers[reindeer]["state"] == reindeers[reindeer]["duration"]:
                reindeers[reindeer]["state"] = reindeers[reindeer]["rest_time"] * -1
        for reindeer in reindeers.keys():
            if reindeers[reindeer]["distance"] >= lead:
                lead = reindeers[reindeer]["distance"]
                leader = reindeer
        reindeers[leader]["points"] += 1
        time += 1
    return max(int(reindeer["points"]) for reindeer in reindeers.values())
    
if __name__ == "__main__":
    print(solution("input.txt"))