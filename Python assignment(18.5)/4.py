def sum_of_first_n_even_numbers(n):
    if n == 1:
        return 2
    else:
        return 2*n + sum_of_first_n_even_numbers(n-1)

n = int(input("Enter a number:"))

print(sum_of_first_n_even_numbers(n))
