'''
    快速排序
    原理：
        利用分治，选择一个元素为基准，将比它小的元素移到左边，将比它大的元素移到右边;
        递归处理两个子列表;
        基线条件：直到子列表没有元素或者只有一个元素，则直接返回该子列表，不用再递归排序
    时间复杂度：
        最优：基准值选择中位数时 O(n*logn)
        平均：O(n*logn)
        最坏：O(n^2)

'''

def quickSort(x):
   
    if len(x) < 2:
        return x
    pivot = x[0]
    less = [elment for elment in x if elment < pivot]
    great = [elment for elment in x if elment > pivot]
    return quickSort(less) + [pivot] + quickSort(great)

list = [2,1,3,4,7]
print(quickSort(list))

'''
    1   2   3,4,7
            3  4,7
                4  7

'''