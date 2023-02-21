def sum_first_n_odd(n):
    if n == 1:
        return 1
    else:
        return 2*n-1 + sum_first_n_odd(n-1)


n = int(input("Enter a number:"))
print(sum_first_n_odd(n))

    