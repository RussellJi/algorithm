# function:实现阶乘
# arg: number
# return: number's factorial
def fact(x):
    if x == 1:
        return x
    else:
        return  x*fact(x-1)

print(fact(3))