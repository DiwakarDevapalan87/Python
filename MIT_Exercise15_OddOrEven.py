def odd(x):
    '''
    x: int

    returns: True if x is odd, False otherwise
    '''
    while x % 2 == 0:
        return "True"
    return "False"
    print(odd(x))

odd(3)