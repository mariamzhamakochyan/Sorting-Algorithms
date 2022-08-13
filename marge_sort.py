def marge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        right = lst[:mid]
        left = lst[mid:]
        marge_sort(right)
        marge_sort(left)
        i = j = k = 0
        while i < len(right) and j < len(left):
            if right[i] <left[j]:
                lst[k] = right[i]
                i += 1
            else:
                lst[k] = left[j]
                j += 1
            k += 1
        while i < len(right):
            lst[k] = right[i]
            i += 1
            k += 1
        while j < len(left):
            lst[k] = left[j]
            j += 1
            k += 1
    return lst
lst = [7, 5, 3, 1]
print(marge_sort(lst))
