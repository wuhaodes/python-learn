"""
Version: 1.0
Author: wuhaodes@qq.com
this is a circle module
"""

def area(r):
    """
    This function calculates the area of a circle
    r: the radius of the circle
    """
    return 3.1416 * r ** 2

def circumference(r):
    """
    This function calculates the circumference of a circle
    r: the radius of the circle
    """
    return 2 * 3.1416 * r

area1 = area(5)
circle1 = circumference(5)

print('周长: %.2f' % circle1)
print('面积: %.2f' % area1)