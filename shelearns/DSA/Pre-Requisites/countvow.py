# h=input("Enter the string  : ")
# k=0
# for character in h:
#     if character=='a' or character=='e' or character=='i' or character=='o' or character=='u': 
#         k= k+ 1
#         print(k)

h = input("Enter the string  : ")
k = 0
for character in h:
    if character in 'aeiouAEIOU':  
        k = k + 1
print(f"Number of vowels: {k}")
