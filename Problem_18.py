#Quadratic Equation Solver: Write a Python program that takes the coefficients (a, b, c) of a quadratic equation as
# input and calculates and prints the real roots (if they exist) or a message indicating the complex roots.

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

discriminant = b**2 - 4*a*c
if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f"The equation has two real and distinct roots: {root1:.2f} and {root2:.2f}")
elif discriminant == 0:
    root = -b / (2 * a)
    print(f"The equation has one real and repeated root: {root:.2f}")
else:
    real_part = -b / (2 * a)
    imaginary_part = math.sqrt(abs(discriminant)) / (2 * a)
    print(f"The equation has complex roots: {real_part:.2f} ± {imaginary_part:.2f}i")