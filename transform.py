"""
Version 1.0
Author: wuhaodes@qq.com
This is a simple program to transform
"""

def temperature_converter(temp, unit):
    """
    This function is used to convert temperature from one unit to another
    :param temp: the temperature to be converted
    """
    if unit == "C":
        return temp * 1.8 + 32
    elif unit == "F":
        return (temp - 32) * 1.8
    else:
        return "Invalid unit"

# Test the function
print(temperature_converter(20, "C")) # Output: 68.0
print(temperature_converter(68, "F")) # Output: 20.0
print(temperature_converter(30, "K")) # Output: Invalid unit

f = float(input("Enter a temperature in Fahrenheit: "))
c = temperature_converter(f, "F")
print(f"{f:.1f}华氏度 is equivalent to {c:.1f}摄氏度")