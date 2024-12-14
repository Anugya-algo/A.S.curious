n=int(input("ENTER NO. OF ITEMS IN LIST : "))
r=[int(input("ENTER THE INTEGERS :")) for i in range(n)]
#r is list
sq=[x**2 for x in r if x%2==0]
print("SQUARE ARE :",sq)

list0=[1,2,3,4]
i=filter(list)