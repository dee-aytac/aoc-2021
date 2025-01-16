from collections import defaultdict

def solution(fname, total_space, needed_space):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    all_folders = set()
    current_path = list()
    folder_contents = defaultdict(list)
    idx = 0
    while idx < len(content):
        line = content[idx]
        if "$" in line:
            command = line.split(' ')[1]
            if command == "cd":
                arg = line.split(' ')[2]
                if arg == "..":
                    current_path.pop()
                else:
                    all_folders.add(arg)
                    current_path.append(arg)
            elif command == "ls":
                file_size = 0
                folders = list()
                while True:
                    idx += 1
                    curr_folder = ("/".join(current_path))
                    p1, p2 = content[idx].split(" ")
                    if "dir" in content[idx]:
                        folders.append(curr_folder + "/" + p2)
                    else:
                        file_size += int(p1)
                    if idx == len(content) - 1 or "$" in content[idx + 1]:
                        break
                folder_contents[curr_folder].append(file_size)
                folder_contents[curr_folder].append(folders)

                
        idx += 1
    not_finished = True
    while not_finished:
        not_finished = False
        for key in folder_contents:
            curr_folder = folder_contents[key]
            children_folders = curr_folder[1]
            if len(children_folders) != 0:
                for child_key in children_folders:
                    child_folder = folder_contents[child_key]
                    if len(child_folder[1]) == 0:
                        curr_folder[0] += child_folder[0]
                        curr_folder[1].remove(child_key)
                not_finished = True

    used_space = total_space - folder_contents["/"][0]
    need_to_delete = needed_space - used_space
    closest_sizes = sorted([[need_to_delete - folder_contents[key][0], folder_contents[key][0]] for key in folder_contents.keys()])
    return sorted([size[1] for size in closest_sizes if size[0] < 0])[0]
if __name__ == "__main__":
    print(solution('input.txt', 70000000, 30000000)) 
