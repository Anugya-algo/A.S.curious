data = [(1, 3), (4, 2), (5, 1)]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)

words = ["apple", "banana", "cherry", "date"]
sorted_words = sorted(words, key=len)
print(sorted_words)  

def custom_sort(val):
    return val % 10  # compare by the last digit

numbers = [15, 42, 33, 24]
sorted_numbers = sorted(numbers, key=custom_sort)
print(sorted_numbers)

# i = list(map(int, input("ENTER THE LIST OF NUMBERS ").split()))

# #sorting compare elements as string
# srt=sorted(i)
# if i[0]>0:
#     result=i[0]-1
#     print(result)
# else :
#     print("result is negative")

i = list(map(int, input("ENTER THE LIST OF NUMBERS ").split()))

positive_numbers = [x for x in i if x > 0]
sorted_numbers = sorted(positive_numbers)

result = 1
for num in sorted_numbers:
    if num == result:
        result += 1  
    elif num > result:
        break  

print(f"The first missing positive integer is: {result}")
