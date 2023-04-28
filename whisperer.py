def messages(path):
    # Open the file located at the given path in binary mode
    with open(path, 'rb') as f:
        # Iterate over each line in the file
        for line in f:
            # Decode the binary data in the line using the ISO-8859-1 encoding and remove whitespace characters
            line_str = line.decode('iso-8859-1').strip()
            # Initialize an empty message string
            message = ""
            # Iterate over each character in the line string
            for ch in line_str:
                # Check if the current character is an ASCII character and is either lowercase or contains an exclamation mark
                if ch.isascii() and (ch.islower() or "!" in ch):
                    # If the condition is true, add the character to the message string
                    message += ch
                # Check if the length of the message string is greater than or equal to 5 and if the last character in the message string is an exclamation mark
                elif message.__len__() >= 5 and message.endswith('!'):
                    # If the condition is true, yield the message string
                    yield message
                    # Reset the message string to an empty string
                    message = ""
        # Close the file
        f.close()

# Prompt the user to enter a path for a file
path = input("Enter the path of the picture\n")
# Call the messages function with the provided path and assign the resulting generator object to the ret variable
ret = messages(path)
# Iterate over each message in the ret generator object and print it to the console
for message in ret:
    print(message)
