def fibbonacci(n):

    a, b = 0,1

    for i in range(n):
        yield a
        a,b = b , a+b

it = fibbonacci(10)

for x in it:
    print(x)

