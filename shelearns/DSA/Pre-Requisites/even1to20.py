i=0
while i<=20:
    if i%2==0:
        print(i)
    i+=1

i=10
while i>0:
    print(i)
    i-=1


# n=input("table of : ")
# i=1
# while i<=10:
#     m=n*i
#     print(f"{n} x {i}= {m}")
#     i+=1
# n is traeted as sting so gives 3
# 33
# 333
# 3333
# 33333    to avoid this input as integer

n=int(input("table of : "))
i=1
while i<=10:
    m=n*i
    print(f"{n} x {i}= {m}")
    i+=1

