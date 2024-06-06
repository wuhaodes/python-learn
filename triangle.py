"""
Version 1.0
Author: wuhaodes@qq.com
this is a triangle program
"""

invalid_triangle_txt: str = "not a valid triangle"


def is_valid_triangle(a: int | float, b: int | float, c: int | float) -> bool:
    """
    This function checks if the given sides of a triangle are valid or not.
    """
    if a + b > c and b + c > a and c + a > b:
        return True
    else:
        return False


def triangle_type(a: int | float, b: int | float, c: int | float) -> str:
    """
    This function returns the type of triangle based on the given sides of a triangle.
    """
    if is_valid_triangle(a, b, c):
        if a == b == c:
            return "equilateral"
        elif a == b or b == c or a == c:
            return "isosceles"
        else:
            return "scalene"
    else:
        return invalid_triangle_txt


# Test the function
print(is_valid_triangle(3, 4, 5))  # True
print(is_valid_triangle(1, 2, 3))  # False
print(triangle_type(3, 4, 5))  # scalene


def triangle_area(a: int | float, b: int | float, c: int | float):
    """
    This function returns the area of a triangle based on the given sides of a triangle.
    """
    if is_valid_triangle(a, b, c):
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5
    else:
        return invalid_triangle_txt


# Test the function
print(triangle_area(3, 4, 5))  # 6.0
print(triangle_area(1, 2, 3))  # not a valid triangle


def triangle_perimeter(a: int | float, b: int | float, c: int | float):
    """
    This function returns the perimeter of a triangle based on the given sides of a triangle.
    """
    if is_valid_triangle(a, b, c):
        return a + b + c
    else:
        return invalid_triangle_txt


# Test the function
print(triangle_perimeter(3, 4, 5))  # 12
print(triangle_perimeter(1, 2, 3))  # not a valid triangle
