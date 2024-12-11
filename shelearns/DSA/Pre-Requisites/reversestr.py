h=input("ENTER THE STRING : ")
l=len(h)
def reverse(h):
    reversed_str= ""
    for i in range(l-1,-1,-1):#[last index,last till 0,step of backwards]
        reversed_str+=h[i]
    return reversed_str
print("Reversed string : ",reverse(h))

   

