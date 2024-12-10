#Tuple unchangeable,fatser than list and set
a=('rih',)
print(len(a))
p=tuple((1,1,1,12,3))
print(p,p[2:5])#SLICING
#out of index range=INDEXERROR
#float index=TYPEERROR
#-1 INDEX IS LAST ITEM


#TO CHANGE CONTENT OF TUPLE=CONVERT IT TO LIST CHANGE AND THEN CONVERT AGAIN
Y=list(p)
Y.append(90)
Y[1]="hi"
Y.remove(1)#only first 1 removed
p=tuple(Y)
print(p)

#PACKING N UNPACKING
first,second,third,*fourth=p# * used with last varibale if variables are less than content so we write so that all leading the last variable content are showed
print(second)
print(*fourth)
#newtuple =('hi',1,12,3,90)
first,*second,third,fourth=p
print(*second)#is * used with in bw variable the values r assiged till content such that
#no. of variables after starred var is equal to number of entries left in tule complete


