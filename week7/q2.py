import math

def CircleArea(radius):
    return math.pi * (radius **2)

radius = float(input("Enter the radius of a circle: "))
area = CircleArea(radius)
print(f"The area of the circle with radius {radius} is : {area:.2f}")
