def pair(lst,t):

    for i in range(len(lst)):                   # For every item in the list
        if (lst[i] == ""):                      # If it is the empty string remove it
            continue
        for j in range(i+1,len(lst)):           # For every item next to the i-item
            if (lst[j] != "" and lst[i]!= ""):  # If each list item is an int and not a string, do the following:
                if ((lst[i] + lst[j]) == t):    # If the 2 nearby list items(pair) sum to t

                    # Replace them with an empty string so we know which pairs to remove later on
                    lst[i] = ""
                    lst[j] = ""

    while ("" in lst):
        lst.remove("")

    return lst
