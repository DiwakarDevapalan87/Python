def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here
    i = exp
    j = base

    if i == 0:
        return 1
    elif i == 1:
        return j
    else:
        for k in range(i-1):
            j = j * base
        print(j)

iterPower(2, 0)
