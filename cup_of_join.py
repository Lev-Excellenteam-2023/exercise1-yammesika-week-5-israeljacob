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

    new_list = [organ if type(organ) != list else join(organ, sep) for list_1 in lists for organ in list_1 + [sep]]

    new_list.pop()
    return new_list


def main():
    print(join([1, 2, 3], ['a', 'b', 'c']))


if __name__ == "__main__":
    main()
