# Python code
# To check if a substring is present in a given string or not

# input strings str1 and substr
string = "geeks for geeks" # or string=input() -> taking input from the user
substring = "geeks" # or substring=input()

# splitting words in a given string
s = string.split()

# checking condition
# if substring is present in the given string then it gives output as yes
if substring in s:
	print("yes")
else:
	print("no")
