#Even or Odd: Write a Python program that takes an integer as input and prints whether it is even or odd.

number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")