def messages(path):
    """
        Extract messages from a file based on specific criteria.

        The function reads a file located at the given path in binary mode. It iterates over each line in the file, decodes
        the line using the ISO-8859-1 encoding, and removes whitespace characters. Messages are extracted based on the
        following criteria:
        - The str_message must consist of ASCII characters.
        - The str_message must be at least 5 characters long.
        - The str_message must end with an exclamation mark '!'.

        Args:
            path (str): The path of the file to read.

        Yields:
            str: Each extracted str_message that meets the criteria.
    """

    with open(path, 'rb') as file:
        for line in file:
            line_str = line.decode('iso-8859-1').strip()
            str_message = ""
            for ch in line_str:
                if ch.isascii() and (ch.islower() or "!" in ch):
                    str_message += ch
                elif str_message.__len__() >= 5 and str_message.endswith('!'):
                    yield str_message
                    str_message = ""
        file.close()


def main():
    path = input("Enter the path of the picture\n")
    ret = messages(path)
    for message in ret:
        print(message)


if __name__ == "__main__":
    main()
