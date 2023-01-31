def multiply_list(input_list):
    total = 1
    for number in input_list:
        total *= number
    return total

print(multiply_list([1, 2, 3, 4, 5]))
# Output: 120
