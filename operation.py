"""
Version: 1.0
Author: wuhaodes@qq.com
This is a sample program to perform basic arithmetic operations in Python.
"""

a = 45
b = 12

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a**b)

a += b
print("After operations:", a)

a -= b
print("After operations:", a)

a *= b
print("After operations:", a)

a /= b
print("After operations:", a)

a //= b
print("After operations:", a)

a %= b
print("After operations:", a)

a **= b
print("After operations:", a)

a *= a + b
print("After operations:", a)

flag0 = 1 == 1
flag1 = 1 == 0
flag2 = 1 < 2
flag3 = 2 > 1
flag4 = flag0 and flag1
flag5 = flag0 or flag1
flag6 = not flag1

print("flag0:", flag0)
print("flag1:", flag1)
print("flag2:", flag2)
print("flag3:", flag3)
print("flag4:", flag4)
print("flag5:", flag5)
print("flag6:", flag6)