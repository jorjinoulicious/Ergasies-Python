def pair(lst,t):

    for i in range(len(lst)):
        if (lst[i] == ""):
            continue
        for j in range(i+1,len(lst)):
            if (lst[j] != "" and lst[i]!= ""):
                if ((lst[i] + lst[j]) == t):
                    lst[i] = ""
                    lst[j] = ""

    while ("" in lst):
        lst.remove("")

    return lst
