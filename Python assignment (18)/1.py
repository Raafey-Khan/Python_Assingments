def f1(n):
    if n==0:
        return 1
    s = f1(n-1)
    print(n)
    return s

f1(10)