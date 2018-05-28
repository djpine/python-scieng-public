def deriv(f, x, h=1.e-9, *params):
    return (f(x + h, *params) - f(x - h, *params))/(2.*h)
