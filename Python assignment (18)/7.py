def squares_num(n):
    if n==0:
        return n #base case do nothing

    else:
        squares_num(n-1)
        print(n*n)

n = int(input("Enter numbers to calculate squares:"))

squares_num(n)