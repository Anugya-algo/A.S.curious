
list=[1,'gigi',2.9,3,4,4,5]
kit=[23,"minion","yui",78]
lit=[list,kit] 

del list[2]
print(list)

list.append(67)
print(list)

list.insert(2,'qwe')
print(list)


list.pop(0) #without index removes last element..pop(index)
print(list)

copy=list.copy() 
print(list)

copy.append(89)
print(copy)

l=list.count(4)
print(l)

list.remove('gigi')#removes only first occurence
list.remove('qwe')
print(list)

kit.extend([lit])
print(lit)

list.index(4)
print(list)

list.reverse()
print(list)

list.sort()

list.clear()

#The enumerate() function allows you to loop through a list (or any iterable) while keeping track of the index.
for index,list in enumerate(list):
    print(index,list)


print(list,kit,lit)
