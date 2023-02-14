def reverse_numbers(n):
    if n==0:
        return 0

    else:
        print(n)
        reverse_numbers(n-1)
n = int(input("Enter the numbers you want to reverse:"))
reverse_numbers(n)