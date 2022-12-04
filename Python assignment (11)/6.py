firstlist = ["Java","Python","SQl"]
secondlist = ["C","Cpp","NoSQL"]

secondlist.insert(0,"Java")
secondlist.insert(1, "Python"   )
secondlist.insert(2,  "SQl")


for e in secondlist:
    print(e,end=" ")