def gargamel(a,b):

    for i in range(a,b+1):          # Till b+1 bc we want to include the given b.The range is [a,b]
        k=0                         # Counter for the consecutive powers(I could actually use a for i in range instead of this)
        sum=0
        for j in str(i):            # Each number converts into a string so we can handle each digit and then for every character(later digit) in that string:
            k+=1
            sum = sum + int(j)**k  # Converting the character back to an int so we can calculate the smurf circumstance


        if (sum == i):              
            return True

    return False
