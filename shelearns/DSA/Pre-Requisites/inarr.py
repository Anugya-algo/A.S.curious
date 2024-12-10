# #USER INPUTS ARRAY LENGTH ,VALUE,SEARCH AND PRINT
from array import *
val=array('i',[])

n=int(input("ENTER THE LENGTH OF ARRAY = "))


for i in range(n):  #i is an iterator
    x=(int(input("ENTER THE VALUE TO FORM ARRAY :")))
    val.append(x)

print("FORMED",val)

z=(int(input("ENTER NUMBER TO BE SEARCHED : ")))

# j=0
# j is counter variable

# for element in val:
#     if element==z:
#         print("The index is :",j)
#         break
#     j+=1
# #function for index
# print(val.index(z))

# # enumerate() Function used coz in array the numbers might repeat

# # The enumerate() function is used to iterate over a collection (like a list or array) and returns both the index and the value of each element.
# # Syntax: enumerate(iterable) returns an iterator of tuples (index, value).


indices = [index+1 for index, value in enumerate(val) if value== z]


if indices:
    print(f"The value {z} is found at indices: {indices}")
else:
    print(f"The value {z} was not found in the array.")




