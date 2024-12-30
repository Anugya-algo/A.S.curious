# with open("data.py","r") as file:
#     freq=file.read(freq)
from collections import Counter
with open("dsa/PRE  REQUISITES/file handling/data.py","r") as file:
    number=[int(line.strip()) for line in file]
           #convert each line strip to integer

freq=Counter(number)#counter for frequency
for number,count in freq.items():
    print(f"{number}:{count}")
"--------------------------------------------------------------------"

freq={}

with open("dsa/PRE  REQUISITES/file handling/data.py","r") as file:
    for line in file:
        num=int(line.strip())
        if num in freq:
            freq[num]+=1
        else:
            freq[num]=1

for number,count in freq.items():
    print(f"{number}:{count}")
"---------------------------------------------------------------------"

strings = ["apple", "banana", "cherry"]

with open("strings.txt", "w") as file:
    for string in strings:
        file.write(string + "\n")#list bni

with open("strings.txt", "r") as file:
    for line in file:
        reversed_string = line.strip()[::-1]  #each strop reverse
        print(reversed_string)
