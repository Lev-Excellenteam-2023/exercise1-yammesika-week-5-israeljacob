def interleave(*organs):
    """
        Interleaves the elements from multiple sequences.

        Args:
            *organs: Variable number of sequences to interleave.

        Returns:
            list: A new list containing interleaved elements from all sequences.

        Example:
            interleave([1, 2, 3], ['a', 'b', 'c']) returns [1, 'a', 2, 'b', 3, 'c'].
    """
    my_list = []
    max_organ = 0

    for organ in organs:
        if len(organ) > max_organ:
            max_organ = len(organ)

    for i in range(0, max_organ):
        for organ in organs:
            if i <= len(organ) + 1:
                my_list.append(organ[i])

    return my_list
