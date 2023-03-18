def checking_HCF(func):

    def wrapper(number1 ,number2):
        
        for i in range(2, min(number1, number2) + 1):

            if number1 % i == 0 and number2 % i == 0:

                return "Not coprime"
            
        return func(number1,number2)
    return wrapper




@checking_HCF
def lets_calculate(number1 , number2):
    smaller = min(number1, number2)

    for i in range(smaller, 0, -1):


        if number1 % i == 0 and number2 % i == 0:


            return i
        
result = lets_calculate(12,6)


print(result)
