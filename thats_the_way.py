import os

def find_deep_files(path):
    deep_files = []
    for file in os.listdir(path):
        if file.startswith("deep"):
            deep_files.append(file)
    return deep_files

path = "C:\\Users\\yisra\\Downloads\\Notebooks-master\\week05\\images"

if os.path.exists(path):
    deep_files = find_deep_files(path)
    print(deep_files)
else:
    print(f"The path {path} does not exist.")
