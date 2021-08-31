# 选择排序
# 原理:每次找出列表中最小的元素,将该元素移到新列表中,继续查找剩余列表

def min(arr):
    min_elment = arr[0]
    min_index = 0
    for i in range(1,len(arr)):
        if arr[i] < min_elment:
            min_elment = arr[i]
            min_index = i
    return min_index

def selectionSort(arr):
    arr_new = []
    for i in range(len(arr)):
        arr_new.append(arr.pop(min(arr)))
    return arr_new

arr = [3,5,4,1]
print(selectionSort(arr))