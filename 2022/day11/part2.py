from collections import defaultdict
from math import prod, lcm

def solution(fname):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    monkeys = dict()
    from collections import defaultdict
    idx = 0
    while idx < len(content):
        monkey = dict()
        monkey_no = int(content[idx].split(' ')[1][0])
        items = content[idx + 1].split(" Starting items: ")[1]
        monkey["items"] = [int(item) for item in    items.split(', ')]
        monkey["operation"] = content[idx + 2].split("  Operation: new = old ")[1]
        monkey["test"] = int(content[idx + 3].split(" by ")[-1])
        monkey["true"] = int(content[idx + 4][-1])
        monkey["false"] = int(content[idx + 5][-1])
        monkeys[monkey_no] =monkey
        idx += 7
    divisor = lcm(*[monkeys[monkey]["test"] for monkey in monkeys.keys()])
    monkey_activity = defaultdict(int)
    for r in range(10000):
        for monkey in monkeys.keys():
            total_items = len(monkeys[monkey]["items"])
            for _ in range(total_items):
                item = str(monkeys[monkey]["items"].pop(0))
                operation = monkeys[monkey]["operation"]
                expr = item + operation

                if "old" in operation:
                    expr = expr.replace("old", item)
                item = eval(expr) % divisor
                test = item % monkeys[monkey]["test"] == 0

                if test:
                    monkeys[monkeys[monkey]["true"]]["items"].append(item)
                else:
                    monkeys[monkeys[monkey]["false"]]["items"].append(item)
                monkey_activity[monkey] += 1
    return prod(list(reversed(sorted(monkey_activity.values())))[:2])
if __name__ == "__main__":
    print(solution('input.txt')) 
