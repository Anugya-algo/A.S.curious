# Defined using functions.
# Use yield instead of return to produce a value,saves memory

def my_generator():
    yield "pink"
    yield 2
    yield 3.990

gen = my_generator()
print(next(gen))  
print(next(gen))  
print(next(gen))  