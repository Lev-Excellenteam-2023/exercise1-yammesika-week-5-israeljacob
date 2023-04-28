def join(*lists, sep="-"):
    # Check if no arguments were passed
    if lists == ():
        return None

    # Initialize an empty list
    new_list = []

    # Loop through each list passed as an argument
    for list1 in lists:
        # Loop through each item in the current list
        for organ in list1:
            # If the item is another list, recursively call the join function
            # with the nested list and separator as arguments and append the result to new_list
            if type(organ) == list:
                new_list.append(join(organ, sep))
            # If the item is not a list, directly append it to new_list
            else:
                new_list.append(organ)

        # Append the separator to new_list after all the items in the current list have been appended
        new_list.append(sep)

    # Remove the last separator appended to new_list and return new_list
    new_list.pop()
    return new_list


# Call the join function with a single list containing the integer 1 as its only item and print the result
print(join([1]))
