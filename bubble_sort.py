#1
def bubble_sort(list):
    for i in range(0, len(list)):
        swap = False
        for j in range(0, len(list) - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                swap = True
                if swap == False:
                    break
    return list
list = [1, 123, 3, 9, 5, 31, 35, 8, 0]
print(sort(list))

#2
def sort(list):
    for i in range(0, n):
        for j in range(i + 1, n):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return list
list = [7, 5, 3, 1]
n = len(list)
print(sort(list))
