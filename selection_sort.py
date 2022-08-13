def selection_sort(lst):
    for i in range(n):
        min_ind = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_ind]:
                min_ind = j
            if min_ind != i
                lst[i], lst[min_ind] = lst[min_ind], lst[i]
    return lst
lst = [1, 6, 2, 85, 4, 76, 34, 0]
n = len(lst)
print(selection_sort(lst))
