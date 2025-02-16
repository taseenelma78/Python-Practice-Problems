#Time Classification: Write a Python program that takes the time in hours (24-hour format) as input and prints
# “Good Morning”, “Good Afternoon”, “Good Evening”, or “Good Night” based on the time.

hours = int(input("Enter the time in hours (0-23): "))

if 5 <= hours < 12:
    print("Good Morning")
elif 12 <= hours < 17:
    print("Good Afternoon")
elif 17 <= hours < 21:
    print("Good Evening")
elif (21 <= hours <= 23) or (0 <= hours < 5):
    print("Good Night")
else:
    print("Invalid input! Please enter a valid hour (0-23).")