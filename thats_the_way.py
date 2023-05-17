import os


def find_deep_files(path):
    """
       Find files in a directory that start with "deep".

       Args:
           path (str): The path of the directory to search for files.

       Returns:
           list: A list of file names that start with "deep".
    """
    list_deep_files = []
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
