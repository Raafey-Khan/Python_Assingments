def decimal_to_octal(n):
    if n > 1:
        decimal_to_octal(n // 8)
    print(n % 8, end="")


decimal_to_octal(10)
