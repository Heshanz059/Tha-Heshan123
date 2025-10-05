import math
A=int(input("Enter the number"))
for i in range(-A,A+1):
      print(' '*(abs(i)),('*'),(' ')*(A+abs(i)+1),('*'))
