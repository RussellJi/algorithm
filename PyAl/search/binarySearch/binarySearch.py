# 二分查找 
# init: low=0 high=len-1
# 原理：在有序的列表中，查找mid，若找到返回元素的索引;
#   若猜测小了，则修改low为mid+1;
#   若猜测大了，则修改high为mid-1;
#   循环直到待查找的元素只剩一个，若没有符合的元素，则返回None
import math
from selectionSort import selectionSort

def binarySearch(list,elment):

    low = 0
    high = len(list) - 1
    count = 0
    #循环直到查找范围只有一个元素
    while low <= high:
        mid = math.floor((low+high) / 2)
        if(elment == list[mid]):
            count+=1
            return mid,count
        elif(elment < list[mid]):
            count+=1
            high = mid - 1
        elif(elment > list[mid]):
            count+=1
            low = mid + 1
    return None

list = [1,3,7,5]
list = selectionSort(list)
print(binarySearch(list,7))
print(binarySearch(list,-2))
print(binarySearch(list,1))
print(binarySearch(list,3))