
list=[1,'gigi',2.9,3,4,4,5]
kit=[23,"minion","yui",78]
lit=[list,kit] 

list.append(34)
print(list)

list.insert(2,'qwe')
print(list)


list.pop(0) #with index removes last element
print(list)

copy=list.copy() 
print(list)

copy.append(89)
print(copy)

l=list.count(4)
print(l)

list.remove('gigi')
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


print(list,kit,lit)
