for i in range(1,6):
    h=i*(" "+"*")
    print(h)

n=int(input("Enter no. of rows : "))

for i in range(1,n+1):#(1,5)
    print(" "* (n-i),end="")#(space 3,2,1,end for so that printing continues in same line)
    print("*" *(2*i-1))