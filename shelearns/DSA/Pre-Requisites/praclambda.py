#P1-FACTORIAL OF NUMBER
p=int(input("ENTER THE NUMBER WHOSE FACTORIAL NEEDS TO BE CALCULATED : "))
factorial=lambda n:1 if n==0 else n*factorial(n-1)
print("FACTORIAL IS: ",factorial(p))

#P2-FILTER STRING SHORTER THAN 4
s=input("INPUT A WORD :").split()
# for i in s :
#     l=len(i) wrong coz i is char so len(i)=0 always
result=list(filter(lambda word:  len(word)>=4,s ))
print(result)