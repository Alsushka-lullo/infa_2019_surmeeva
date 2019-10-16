our_list1 = [1, 3, 5, 6, 7, 8]
our_list2 = [2, 3, 4]


def difference(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1 - set2) # можно написать в 1 строку


print(difference(our_list1, our_list2))

# 9/10
