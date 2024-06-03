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
    
def in_cm_transform(len, unit):
    """
    This function is used to convert length from inches to centimeters or reverse
    """
    if unit == "in" or unit == "inches" or unit == "inch" or unit == "英寸":
        return len * 2.54
    elif unit == "cm" or unit == "centimeters" or unit == "centimeter" or unit == "厘米":
        return len / 2.54
    else:
        return "Invalid unit"
 


# Test the function
f = float(input("Enter a temperature in Fahrenheit: "))
c = temperature_converter(f, "F")
print(f"{f:.1f}华氏度 is equivalent to {c:.1f}摄氏度")   
    
    
def percent_to_grade(score):
    """
    This function is used to convert a score to a letter grade
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "E"

# Test the function
score = float(input("Enter a score: "))
grade = percent_to_grade(score)
print(f"The grade is {grade}")
