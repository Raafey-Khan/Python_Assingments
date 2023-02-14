def print_multiples(n, m):
    if n == 0:
        return
    print_multiples(n - 1, m-1)
    print(n * m)

print_multiples(2,4)