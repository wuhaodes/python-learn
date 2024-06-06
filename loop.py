"""
Version 1.0
Author: wuhaodes@qq.com
This program used to learn loops in Python.
"""
import random

total = 0
for i in range(1, 101):
    total += i
print(total)

sum = 0
for i in range(2, 101, 2):
    sum += i
print(sum)

def guess_random_number(n):
    random_number = random.randint(1, n)
    guess = 0
    while guess!= random_number:
        guess = int(input("Guess a number between 1 and {}: ".format(n)))
        if guess < random_number:
            print("Too low, try again!")
        elif guess > random_number:
            print("Too high, try again!")
    print("Congratulations, you guessed the number!")

# guess_random_number(100)


"""
打印乘法口诀表
"""
def multiplication_table():
    for i in range(1, 10):
        for j in range(1, i+1):
            print("{:2d} x {:2d} = {:2d}".format(j, i, i*j), end="\t")
        print()

multiplication_table()