
def sum(x):
    if len(x) == 1:
        return x[0]
    else:
        return x[0] + sum(x[1:])

list = [1,3,5]

print(sum(list))

# 1 + sum(3,5)
# 1+ 3+sum(5)