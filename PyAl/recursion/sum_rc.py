'''
    sum:使用递归和分治求和
    arg: list
    return: number
    
    思路: 
        基准条件: 当列表没有元素或者只有一个元素的时候

    注意: 求列表的长度len(list)
          当列表只有一个元素时，其值为x[0]
'''
def sum(x):
    if len(x) == 1:
        return x[0]
    else:
        return x[0] + sum(x[1:])

list = [1,3,5]
print(sum(list))

# 1 + sum(3,5)
# 1 + 3 + sum(5)
# 1 + 3 + 5 = 9