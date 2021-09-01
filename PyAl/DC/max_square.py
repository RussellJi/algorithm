'''
    问题描述：在一个给定了边长的长方形中，求可以将长方形等分的最大的正方形
    解决思路：
            小区域中满足条件的最大的正方形也是整个区域中满足条件的正方形；
            分治，将整个区域划分为由以宽为边长的正方形组成的长方形，以及剩余部分的长方形；
            递归求剩余长方形中的满足条件的正方形。
            
    基准条件（跳出递归的条件）：长和宽相等。
'''
def max_square(x):
    if x[0] == x[1]:
        return x[0]
    elif x[0] > x[1]:
        return max_square((x[0]-x[1]),x[1])
    else:
        return max_square(((x[1]-x[0]),x[0]))

def max_square2(x):
    if x[0] == x[1]:
        return x[0]
    elif x[0] > x[1]:
        list = []
        list.append(x[0]-x[1])
        list.append(x[1])
        return max_square2(list)
    else:
        list = []
        list.append(x[1]-x[0])
        print("1:",list)
        list.append(x[0])
        print("list:",list)
        return max_square2(list)

tuple = (4,6)
list = [640,1680]

print(max_square2(list))

