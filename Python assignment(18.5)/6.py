def square(n):
    if n==1:
        return 1
    
    else:
        return n**3 + square(n-1)

n = int(input("Enter a number:"))

print(square(n))