def check_triangle(func):

    def wrapper(side1,side2,side3):

        if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:

            return func(side1,side2,side3)
        
        else:
            return "Invalid triangle"
        
    return wrapper



@check_triangle
def calculate_perimeter(side1,side2,side3):

    perimeter = side1 + side2 + side3

    return perimeter

print(calculate_perimeter(3,4,5))

print(calculate_perimeter())