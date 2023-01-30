print("")
sample_dict = { 'C': 92, 'Java': 66, 'Python': 85 }

for a,i in sample_dict.items(): 
    if i in range(1,50):
        print(i,"starting point")
    elif i in range(1,70):
        print(i,"Lowest point")
    elif i in range(1,100):
        print(i,"Middle point")
        

      