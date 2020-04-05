import sys

def merge(data):
    length = len(data)
    if length < 2:
        return data

    list1 = []
    list2 = []
    mid = data.pop(0)
    length = len(data)
    for i in range(length):
        if data[i] < mid:
            list1.append(data[i])
        else:
            list2.append(data[i])
    return merge(list1)+[mid]+merge(list2)

a = merge([0, 3, 8, 5, 4, 54, 33, 2, 4, 14])
print(a)
