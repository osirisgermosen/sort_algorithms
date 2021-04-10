def insertion_sort(list):
    for i in range(1, len(list)):
        j = i - 1
        element_next = list[i]

        while (list[j] > element_next) and (j >= 0):
            list[j + 1] = list[j]
            j = j - 1
        list[j + 1] = element_next
    return list


listValues = [7, 6, 5, 4, 3, 2, 1]
print(insertion_sort(listValues))
