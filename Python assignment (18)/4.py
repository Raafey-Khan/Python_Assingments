def odd(n):
    if n==a:
        return 0

    else:
        s = odd(n+1)
        
        print(n*2-1)
        
        return s

a = int(input("Enter how much odd numbers you want:"))
odd(1)