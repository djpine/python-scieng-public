string1 = "How"
string2 = "are you my friend?"
int1 = 34
int2 = 942885
float1 = -3.0
float2 = 3.141592653589793e-14
print(string1)
print(string1 + ' ' + string2)
print('A. {} {}'.format(string1, string2))
print('B. {0:s} {1:s}'.format(string1, string2))
print('C. {0:s} {0:s} {1:s} - {0:s} {1:s}'
      .format(string1, string2))
print('D. {0:10s}{1:5s}'          # reserves 10 & 5 spaces,
      .format(string1, string2))  # respectively for 2 strings
print(' **')
print(int1, int2)
print('E. {0:d} {1:d}'.format(int1, int2))
print('F. {0:8d} {1:10d}'.format(int1, int2))
print(' ***')
print('G. {0:0.3f}'.format(float1))  # 3 decimal places
print('H. {0:6.3f}'.format(float1))  # 6 spaces, 3 decimals
print('I. {0:8.3f}'.format(float1))  # 8 spaces, 3 decimals
print(2 * 'J.  {0:8.3f}   '.format(float1))
print(' ****')
print('K. {0:0.3e}'.format(float2))
print('L. {0:12.3e}'.format(float2))  # 12 spaces, 3 decimals
print('M. {0:12.3f}'.format(float2))  # 12 spaces, 3 decimals
print(' *****')
print('N. 12345678901234567890')
print('O. {0:s}--{1:8d},{2:10.3e}'
      .format(string2, int1, float2))

"""
Introduction to Python for Science & Engineering
by David J. Pine
Code last edited: 2018-09-17

Scripting example with formatted print output
"""
