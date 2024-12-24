A= [1, 2, 3, 4]
B= [3, 4, 5, 6]
A=set(A)
B=set(B)

print(A.union(B))        
print(A.intersection(B)) 

################################

# a=set(input("enter set 1 :"))
# b=set(input("enter set 2 :"))

# if a.intersection(b)==0:
#     print("it is disjoint.")

# else:
#     print("not disjoint")

a = set(input("Enter set 1 (comma-separated values): ").split(","))
b = set(input("Enter set 2 (comma-separated values): ").split(","))

if a.isdisjoint(b):
    print("It is disjoint.")
else:
    print("Not disjoint.")


