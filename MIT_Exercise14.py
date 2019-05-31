def fourthPower(x):
    '''
    x takes in int or float and returns fourth power
    '''
    for i in range(1, 3, 1):
        ans = x*x
        x = ans
    print(ans)

fourthPower(3)
