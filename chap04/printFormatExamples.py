string1 = "How"
string2 = "are you my friend?"
int1 = 34
int2 = 942885
float1 = -3.0
float2 = 3.141592653589793e-14
print(string1)
print(string1 + ' ' + string2)
print(' 1. {} {}'.format(string1, string2))
print(' 2. {0:s} {1:s}'.format(string1, string2))
print(' 3. {0:s} {0:s} {1:s} - {0:s} {1:s}'
      .format(string1, string2))
print(' 4. {0:10s}{1:5s}'
      .format(string1, string2))
print(' **')
print(int1, int2)
print(' 6. {0:d} {1:d}'.format(int1, int2))
print(' 7. {0:8d} {1:10d}'.format(int1, int2))
print(' ***')
print(' 8. {0:0.3f}'.format(float1))
print(' 9. {0:6.3f}'.format(float1))
print('10. {0:8.3f}'.format(float1))
print(2*'11.  {0:8.3f}'.format(float1))
print(' ****')
print('12. {0:0.3e}'.format(float2))
print('13. {0:10.3e}'.format(float2))
print('14. {0:10.3f}'.format(float2))
print(' *****')
print('15. 12345678901234567890')
print('16. {0:s}--{1:8d},{2:10.3e}'
      .format(string2, int1, float2))
