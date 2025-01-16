
def solution(fname, input_bag):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    container_bags = set()
    bags_to_check = set()
    for line in content:
        main_bag, contained = line.split(' bags ')
        if input_bag in contained:
            bags_to_check.add(main_bag)
            container_bags.add(main_bag)
    while True:
        idx = 0
        found_new = False
        new_bags = set()
        while idx < len(content):
            for bag in bags_to_check:
                main_bag, contained = content[idx].split(' bags ')
                if bag in contained:
                    found_new = True
                    new_bags.add(main_bag)
                    container_bags.add(main_bag)
            idx += 1
        if found_new == False:
            return len(container_bags)
        bags_to_check = new_bags

if __name__ == "__main__":
    print(solution('input.txt', "shiny gold")) 
