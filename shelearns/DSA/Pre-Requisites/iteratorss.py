#iterators : transverses a collection

listt=[1,2,3,4,5,6,7,8,9,10]
iteratorr=iter(listt)

for i in range(2,7):
    print(next(iteratorr))
#prints StopIteration when list finishes

# Question : Implement an iterator class for a custom range.
print("----------------------------------")
class CustomRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.current < self.end:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration
# Using the CustomRange iterator
custom_range = CustomRange(2, 8)
for num in custom_range:
    print(num)



print("-"*35)

listt = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
iteratorr = iter(listt)

# Skip the first  elements
for _ in range(1):
    next(iteratorr)

# Print elements from 2nd to 7th
for i in range(2, 8):
    print(next(iteratorr))

