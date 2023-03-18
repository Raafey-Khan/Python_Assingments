def even_number(n):
    
    i = 2

    count = 0

    while count< n:

        yield i

        i+=2

        count+=1

it = even_number(5)

for i in it:
    print(i)