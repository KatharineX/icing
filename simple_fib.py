###Simple fibonacci code

import sys

n = input("Enter your number: ")

def inside_out(n):
    n = int(n)
    if n == 0:
         return 0
    elif n == 1:
        return 1
   
    return inside_out(n-2) + inside_out(n-1)

print(inside_out(n))
