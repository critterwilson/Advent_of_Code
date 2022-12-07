class Directory:
    def __init__(self, name:str, size:int, parent):
        self.size = size
        self.name = name
        self.parent = parent
        self.children = []

    def add_child(self, x):
        self.children.append(x)
        self.size = sum([c.size for c in self.children])

        parent = self.parent
        while parent != None:
            parent.size += x.size
            parent = parent.parent
    
    def __str__(self):
        self.name

class File:
    def __init__(self, name:str, size:int, parent:Directory):
        self.size = size
        self.name = name
        self.parent = parent

    def __str__(self):
        self.name

class FileSystem:
    def __init__(self, input:str):
        self.root = Directory("/", 0, None)
        self.create_file_system(input)

    def create_file_system(self, input:str):
        current_dir = self.root
        for line in input:
            x = line.strip().split(" ")
            if (x[0] == "$"): # action
                if x[1] == "ls":
                    pass
                elif x[1] == "cd":
                    if x[2] == "..":
                        current_dir = current_dir.parent
                    else:
                        for child in current_dir.children:
                            if child.name == x[2]:
                                current_dir = child
                                break
            else: # directory information
                if x[0].isdigit():
                    current_dir.add_child(File(x[1], int(x[0]), current_dir))
                if x[0] == "dir":
                    current_dir.add_child(Directory(x[1], 0, current_dir))

    def get_directory_sizes(self):
        def _traverse_directories(node:Directory, l:list): 
            l.append((node.name, node.size))
            if not node.children or not ([x for x in node.children if type(x) == Directory]):
                return
            for child in node.children:
                if type(child) == Directory:
                    _traverse_directories(child, l)
        sizes = []
        _traverse_directories(self.root, sizes)               
        return sizes

    def get_directories_less_than(self, val:int):
        sizes = self.get_directory_sizes()
        less_than_sizes = [x for x in sizes if x[1] < val]
        return less_than_sizes

    def get_directories_greater_than(self, val:int):
        sizes = self.get_directory_sizes()
        greater_than_sizes = [x for x in sizes if x[1] >= val]
        return greater_than_sizes


def test():
    o = open("../Input/test_input.txt")
    s = o.readlines()
    o.close()

    f = FileSystem(s)
    sizes = f.get_directories_less_than(100000)
    print(sizes)
    print(f"Total space less than 100000: {sum([x[1] for x in sizes])}\n")


def challenge1():
    o = open("../Input/day7_input.txt")
    s = o.readlines()
    o.close()

    f = FileSystem(s)
    sizes = f.get_directories_less_than(100000)
    print(sizes)
    print(f"Total space less than 100000: {sum([x[1] for x in sizes])}\n")


def challenge2():
    o = open("../Input/day7_input.txt")
    s = o.readlines()
    o.close()

    f = FileSystem(s)
    total_space = 70000000
    used_space = [x for x in f.get_directory_sizes() if x[0] == "/"][0][1]
    update_space = 30000000
    needed_space = update_space - (total_space-used_space)
    print(needed_space)

    sizes = f.get_directories_greater_than(needed_space)
    print(sizes)
    print(f"Total: {min(sizes, key=lambda x: x[1])}")

test()
challenge1()
challenge2()