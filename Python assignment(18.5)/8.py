def add(n):
    if n==1:

        return 1

    else:
        return n+add(n-1)

n = int(input("Enter a number:"))

print(add(n))