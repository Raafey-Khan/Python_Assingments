def convert_to_dict(list1, list2):
    return {list1[i]: list2[i] for i in range(len(list1))}

list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']

result = convert_to_dict(list1, list2)
print(result)
