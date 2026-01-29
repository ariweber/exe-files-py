import os

print(os.getcwd())

for item in os.listdir():
    print(item)


def move_and_list(path):
    original = os.getcwd()
    os.chdir(path)
    print(os.listdir())
    os.chdir(original)

   
