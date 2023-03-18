def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_first_n_primes(n):
    prime_count = 0
    num = 2
    while prime_count < n:
        if is_prime(num):
            print(num, end=' ')
            prime_count += 1
        num += 1

# Example usage
print_first_n_primes(10)


    