def even_reverse(n):
    if n == 0:
        return  # Base case, do nothing

    else:
        print(n*2)
        even_reverse(n-1)

a = int(input("Enter how many even numbers you want: "))
even_reverse(a)
