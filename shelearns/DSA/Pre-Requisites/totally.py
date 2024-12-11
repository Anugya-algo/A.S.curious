lst = [1, 2, 3, 4, 5]
def sum(x, y):
    return x + y
total = 0
for e in lst:
    total = sum(total, e)
print(total)



from functools import reduce
lst = [1, 2, 3, 4, 5]
def sum(x, y):
    return x + y
total = reduce(sum, lst)
print(total)