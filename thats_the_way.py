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
    return [file for file in os.listdir(path) if file.startswith("deep")]



def print_file_names():
    """
        Print the names of files starting with "deep" in a specified directory.

        The function retrieves the list of file names from a specified directory and prints the names of files that start
        with the prefix "deep".
    """
    path = "C:\\Users\\yisra\\Downloads\\Notebooks-master\\week05\\images"

    if os.path.exists(path):
        list_deep_files = find_deep_files(path)
        print(list_deep_files)
    else:
        print(f"The path {path} does not exist.")


def main():
    print_file_names()


if __name__ == "__main__":
    main()
