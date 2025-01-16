
def get_children(parent_bag, bags, children):
    parent_contents = bags[parent_bag]
    for child in parent_contents.split(', '):
        bag_color = child[2:].replace('.', '')
        if "no other" in child:
            return
        bag_count = int(child[0])
        if bag_color in children:
            children[bag_color] += bag_count
        else:
            children[bag_color] = bag_count
        for _ in range(bag_count):
            get_children(bag_color, bags, children)

def solution(fname, input_bag):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    bags = dict()
    for bag in content:
        bag = bag.replace(" bags", "").replace(" bag", "")
        bag = bag.split("contain ")
        bags[bag[0].strip()] = bag[1]
    children = dict()
    get_children(input_bag, bags, children)
    return sum(children.values())


if __name__ == "__main__":
    print(solution('input.txt', "shiny gold")) 

