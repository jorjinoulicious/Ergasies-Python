def FileHash(fl):
    fl = open(fl, "r")
    fl_read = fl.readlines()
    fl_seperation = "".join(fl_read)
    fl.close()

    segments = []

    for i in range(1,int(len(fl_seperation)/16)+1):
        cut_str = fl_seperation[((i*16)-16):i*16]

        segments.append(cut_str)



    to_ascii = []
    for elements_16 in segments:             #for every 16-ada
        to_ascii_16 = []
        for char in elements_16:             #for every char in the 16-ada
            to_ascii_16.append(ord(char))
        to_ascii.append(to_ascii_16)


    add_vectors = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for vector in to_ascii:
        for i in range(len(vector)):
            add_vectors[i] += vector[i]


    for i in range(len(add_vectors)):
        add_vectors[i] = add_vectors[i] % 256


        add_vectors[i] = hex(add_vectors[i])
        remove_0x = add_vectors[i][2:]

        while ( len(remove_0x) < 2):
            remove_0x = "0" + remove_0x

        add_vectors[i] = remove_0x





    return "".join(add_vectors)
