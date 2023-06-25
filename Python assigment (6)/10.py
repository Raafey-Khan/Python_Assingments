def cn():      #cn is the main func
     r = int(input("Enter the real part:-"))
     i = int(input("Enter the image part:-"))   
     print(r)
     print(i)
     r.real
     i.imag
     if r>i:
         print("real part is bigger ", r)
     elif i>r:
         print("imaginary part is bigger", i)
     else:
         print("No difference between real and imag")
     print(complex(r, i))

cn()  
