l1 = {1,2,3,4,5,6}

it = iter(l1)

while l1:
    try:
         print(next(it))
    except:
         StopIteration
         break
