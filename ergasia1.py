def gargamel(a,b):
    for i in range(a,b+1):
        k=0
        sum=0
        for j in str(i):
            k+=1
            sum = sum + int(j)**k


        if (sum == i):
            return True

    return False
