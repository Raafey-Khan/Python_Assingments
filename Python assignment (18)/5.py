def even(n):

    if n==0:
        return 1
    else:
        s = even(n-1)
        print(n*2,end="")

        return s

n = int(input("enter how much even number you want you want:"))



eval(n)