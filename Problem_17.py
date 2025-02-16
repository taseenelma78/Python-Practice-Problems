#Triangle Type Checker: Write a Python program that takes three sides of a triangle as input and determines
#whether it forms an equilateral, isosceles, or scalene triangle.

side1 = float(input("Enter first side: "))
side2 = float(input("Enter second side: "))
side3 = float(input("Enter third side: "))


if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    if side1 == side2 == side3:
        print("The triangle is Equilateral.")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("The triangle is Isosceles.")
    else:
        print("The triangle is Scalene.")
else:
    print("Invalid triangle! The sum of any two sides must be greater than the third side.")