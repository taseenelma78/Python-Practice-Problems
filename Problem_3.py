#String Reverse: Write a Python function to reverse a given string and return the reversed string.

string = "python"
reverse = ""
for i in string:
    reverse = i + reverse
print(reverse)