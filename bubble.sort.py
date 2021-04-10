
def bubble_sort(list):
    last_element_index = len(list)-1
    for pass_number in range(last_element_index, 0, -1):
        for index in range(pass_number):
            if list[index] > list[index+1]:
                list[index], list[index+1] = list[index+1], list[index]
    return list


listValues = [7, 6, 5, 4, 3, 2, 1]
print(bubble_sort(listValues))
