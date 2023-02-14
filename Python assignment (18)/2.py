def f2(n):
    if n==a:
        return 0
    s = f2(n+1)
    print(n)
    return s

n = int(input("Enter a value for n: "))
a = int(input("Enter a value for n:"))
f2(n)
