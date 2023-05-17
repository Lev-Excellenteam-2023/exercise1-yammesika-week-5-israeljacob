def join(*lists, sep="-"):
    """
        Joins multiple lists into a single list, with an optional separator between elements.

        Args:
            *lists: Variable number of lists to join.
            sep (str): Separator to insert between elements (default is '-').

        Returns:
            list: A new list containing the joined elements from all lists.

        Example:
            join([1, 2, 3], ['a', 'b', 'c']) returns [1, 2, 3, '-', 'a', 'b', 'c'].
    """
    if lists == ():
        return None

    new_list = []

    for list1 in lists:
        for organ in list1:
            if type(organ) == list:
                new_list.append(join(organ, sep))
            else:
                new_list.append(organ)

        new_list.append(sep)

    new_list.pop()
    return new_list


print(join([1]))
