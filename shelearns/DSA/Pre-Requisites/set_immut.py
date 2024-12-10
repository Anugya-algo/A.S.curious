#SET ={} unordered and immutable.doesnt repeat content,but add/remove,no copy,no indexing

s={1,2,3,4,5,6}
print(dir(s))#list all atributes and methods for set
print(len(s))
s.add(9)
s.remove(5)
s.pop()
s.clear()
#duplicates are independent from original
#copy- shallow is dependent still references, deep is independent