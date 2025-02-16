#String Palindrome: Write a Python function to check if a given string is a palindrome or not.

input = 'racecar'
reverse = input[::-1]
if reverse == input:
    print(f'{input} is a palindrome')
else:
    print(f'{input} in not a palindrome')