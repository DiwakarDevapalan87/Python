def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    d = a*x*x + b*x + c*x
    print(d)

evalQuadratic(10, 20, 30, 5)
