n=int(input("enter the no. to be examined : "))
if n<=1:
    print("Not a prime Numnber")
elif n==2:
    print(" prime no.")
else:
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1

if count>2:
    print("Not a prime no. ")
else:
    print("Prime no. ")

 