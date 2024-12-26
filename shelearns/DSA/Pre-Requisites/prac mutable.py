# Given an array of integers nums and an integer target,
# #  return the indices of the two numbers that add up to target.
# a=int(input("ENTER ARRAY ")).split()
# b=int(input("ENTER THE DESIRED SUM :"))
# sum=0
# for b in a:
#     if sum=b
#     print(enumerate(b))

a = list(map(int, input("Enter array elements separated by space: ").split()))
target = int(input("Enter the desired sum: "))

# Created dictionary to store seen numbers and their indices
seen = {}
#made dict
    #index,value
for i, num in enumerate(a):
    complement = target - num
    if complement in seen:#if complement exist in dict
        print(f"Indices: {seen[complement]}, {i}")#prints indices
        break
    seen[num] = i
else:
    print("No two numbers add up to the target sum.")
