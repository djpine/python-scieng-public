def test(s, v, t, l, a):
    s = "I am doing fine"
    v = np.pi**2
    t = (1.1, 2.9)
    l[-1] = 'end'
    a[0] = 963.2
    return s, v, t, l, a


import numpy as np

s = "How do you do?"
v = 5.0
t = (97.5, 82.9, 66.7)
l = [3.9, 5.7, 7.5, 9.3]
a = np.array(l)

print('*************')
print("s = {0:s}".format(s))
print("v = {0:5.2f}".format(v))
print("t = {}".format(t))
print("l = {}".format(l))
print("a = "),           # comma suppresses line feed
print(a)
print('*************')
print('*call "test"*')

s1, v1, t1, l1, a1 = test(s, v, t, l, a)

print('*************')
print("s1 = {0:s}".format(s1))
print("v1 = {0:5.2f}".format(v1))
print("t1 = {}".format(t1))
print("l1 = {}".format(l1))
print("a1 = "),          # comma suppresses line feed
print(a1)
print('*************')
print("s = {0:s}".format(s))
print("v = {0:5.2f}".format(v))
print("t = {}".format(t))
print("l = {}".format(l))
print("a = "),
print(a)
print('*************')

"""
Introduction to Python for Science & Engineering
by David J. Pine
Code last edited: 2018-09-18

Test about how different kinds of variables, mutable
and immutable, are passed to functions
"""
