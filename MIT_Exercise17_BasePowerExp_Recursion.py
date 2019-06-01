def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        return base * recurPower(base, exp-1)

recurPower(2, 3)