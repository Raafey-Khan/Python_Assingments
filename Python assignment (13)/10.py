tuple1 = (11,[22,33],44,55)

tuple2 = list(tuple1)

tuple2[1] = (222,33)

Finaltuple = tuple(tuple2)

print(Finaltuple)

