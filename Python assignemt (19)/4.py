def squares(n):
    for i in range(1, n+1):
        yield i*i


s = squares(10)

for i in s:
    print(i)



