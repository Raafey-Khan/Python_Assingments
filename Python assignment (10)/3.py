num = int(input("Enter the number u want to calculate the cubes of:-"))
sum = 0
print("The cubes of",num,'are')
for i in range(1,num+1):
    sum=sum+(i*i*i)
    print(sum)
    