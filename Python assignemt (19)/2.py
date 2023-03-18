def odd_numbers(n):

    i = 1

    count = 0

    while count < n:

        yield i

        i+=2

        count+=1


f = odd_numbers(5)

for i in f:
    print(i)

    