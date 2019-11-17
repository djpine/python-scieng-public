import numpy as np
import scipy.integrate


def f(x):
    return 1.0 / (1 + x * x)


i1, er1 = scipy.integrate.quad(f, -1, 1)
i1exact = np.pi / 2.
print('\n*************************************************')
print('\nI1 = {} \u00B1 {}'.format(i1, er1))
print('  relative error {}'.format((i1 - i1exact) / i1exact))


def g(x):
    a = np.exp(x) + x + 1.0
    return 1.0 / (a * a + np.pi ** 2)


i2, er2 = scipy.integrate.quad(g, -np.inf, np.inf)
i2exact = 2. / 3.
print('\nI2 = {} \u00B1 {}'.format(i2, er2))
print('  relative error {}'.format((i2 - i2exact) / i2exact))
print('\n*************************************************\n')
