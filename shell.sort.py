def shell_sort(list):
    distance = len(list) // 2
    while distance > 0:
        for i in range(distance, len(list)):
            temp = list[i]
            j = i
            while j >= distance and list[j - distance] > temp:
                list[j] = list[j - distance]
                j = j - distance
            list[j] = temp
        distance = distance // 2
    return list


list = [44, 16, 83, 7, 67, 21, 34, 45, 10]
print(shell_sort(list))