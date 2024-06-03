"""
Version 1.0
Author: wuhaodes@qq.com
This is a function to use if-else statements in Python.
"""


def f(x: int) -> int:
    """
    f(x) ={3x-5,(x>1) x+2,(-1<=x<=1) 5x+3,(x<-1)}
    """
    if x > 1:
        return 3 * x - 5
    elif x >= -1:
        return x + 2
    else:
        return 5 * x + 3


def f1(x: int) -> int:
    """
    f(x) ={3x-5,(x>1) x+2,(-1<=x<=1) 5x+3,(x<-1)}
    """
    if x > 1:
        return 3 * x - 5
    else: 
        if x >= -1:
            return x + 2
        else:
            return 5 * x + 3

print(f(2))  # Output: 1
print(f(0))  # Output: 2
print(f(-2))  # Output: -7

print(f1(3)) # Output: 4
