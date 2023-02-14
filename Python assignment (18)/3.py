def odd_number(n):
    if n==1:
        print(1)

    else:
        s = odd_number(n-1)
        print(n*2-1)
        return s
        


n = int(input("Enter how much odd numver you want:"))

odd_number(n)
