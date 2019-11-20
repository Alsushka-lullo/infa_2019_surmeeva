list1 = [1, 5, 6, 3, 66, 2, 6, 2, 2]


def selection_sort(list_tm):
    # почему list_tm?
    minimum_ind = 0
    for i in range(len(list_tm)):
        for k in range(i, len(list_tm)):
            if list_tm[k] == min(list_tm[i:]):
                # это будет работать, но это не эффективно.
                # Ты каждый раз ищешь минимум -
                # это О(N^2) поисков синимумов, каждый по O(N).
                # тогда итогово сортировка будет O(N^3).
                # А сортировка выбором это О(N^2)
                minimum_ind = k
                break
        list_tm[i], list_tm[minimum_ind] = list_tm[minimum_ind], list_tm[i]
    return(list1)
    # почему ты работаешь над одним списком, а возвращаешь другой


list2 = [3, 2, 1]
print(selection_sort(list1))
print(selection_sort(list2))  # эта строка работает не так, как должна
# поэтому задача не решена

# 3/10 (не решено)
