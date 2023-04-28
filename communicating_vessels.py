def interleave(*organs):
    # Create an empty list to store the interleaved elements
    my_list = []
    # Find the length of the longest argument
    max_organ = 0
    for organ in organs:
        if len(organ) > max_organ:
            max_organ = len(organ)
    # Loop through each index from 0 to max_organ
    for i in range(0, max_organ):
        # Loop through each argument and append the i-th element to my_list
        for organ in organs:
            # Check if i is within the range of valid indexes for the current argument
            if i <= len(organ) + 1:
                my_list.append(organ[i])
    return my_list
