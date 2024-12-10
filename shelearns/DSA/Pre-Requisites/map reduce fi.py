def square(x):
    return x*x
l=[2,3,4,5]
# sq_l=[]
# for item in l:
#     sq_l.append(square(item))

# print(sq_l)

#MAP all 3 Higher order function takes other functions as their arguments. 
sq_l=list(map(square,l))#(function to apply,list)
print(sq_l)

cb_l=list(map(lambda x:x*x*x,l))#(function to apply,list)
print(cb_l)


#FILTER
def filter_fun(a):
    return a>4#which is true is displayed

fil_l=list(filter(filter_fun,sq_l))
print(fil_l)

from functools import reduce

def thesum(x,y):
    return x+y

sum1=reduce(thesum,l)
print(sum1)