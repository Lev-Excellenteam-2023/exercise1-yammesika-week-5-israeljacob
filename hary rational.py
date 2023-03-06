import os
import re


directory = input("Enter the directory to the folder\n")

# Loop through each file in the directory.
for file in os.listdir(directory):

    # Get the full path of the file.
    my_path = os.path.join(directory, file)

    # Get the filename without the path.
    old_name = os.path.basename(my_path)

    # Try to open the file for reading. If it's not possible due to a UnicodeDecodeError, continue to the next file.
    try:
        with open(my_path) as f:
            text = f.read()
            f.close()
    except UnicodeDecodeError as e:
        continue

    # Split the text by "Chapter " and take the second part.
    new_name = text.split("Chapter ")[1]

    # Split the result by "<" and take the first part.
    new_name = new_name.split("<")[0]

    # Split the result by ":" and store it in a temporary variable.
    temp = new_name.split(":")

    # If the first part of the result has less than 3 characters, add "0" to the beginning until it has 3 characters.
    while temp[0].__len__() < 3:
        temp[0] = "0".__add__(temp[0])

    # Rename the file using the new name.
    os.rename(my_path, os.path.join(directory, temp[0] + temp[1] + ".html"))

