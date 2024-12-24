#Problem: Write a function that accepts a list of numbers and returns a list of tuples, where each tuple contains the index and value of the number, but only for even values.
l = list(map(int, input("Enter the numbers to be in the list (space-separated): ").split()))

# input() gets the raw user input as a string (e.g., "1 2 3 4").
# .split() breaks the string into a list of substrings (e.g., ["1", "2", "3", "4"]).
# map(int, ...) converts each string element to an integer (e.g., [1, 2, 3, 4]).
# list() converts the result of map() into a list.

#enumerate to get both index+value
for index, value in enumerate(l):
    if value % 2 == 0:
        print((index, value)) 

def merge_lists(names, ages):
    return list(zip(names, ages))

names = ["A", "n", "u"]
ages = [25, 30, 35]

result = merge_lists(names, ages)
print(result)
