import os

print(os.getcwd())

for item in os.listdir():
    print(item)


def move_and_list(path):
    original = os.getcwd()
    os.chdir(path)
    print(os.listdir())
    os.chdir(original)

def print_all_files(path):
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if os.path.isfile(full_path):
            print(item)
        else:
            print_all_files(full_path)    



   

def collect_py_files(path):
    py_files = []
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if os.path.isfile(full_path) and item.endswith(".py"):
            py_files.append(full_path)
        elif os.path.isdir(full_path):
            py_files.extend(collect_py_files(full_path))
    return py_files


