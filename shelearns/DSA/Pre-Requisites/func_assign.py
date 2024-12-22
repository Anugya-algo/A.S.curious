def counter():  
    count = 0 

    def increment():  
        nonlocal count  # Refers to the `count` in the enclosing scope
        count += 1  
        return count  

    return increment  

counter1 = counter()  
print(counter1())  # First call to `counter1()`, increments count to 1
print(counter1())  # Second call to `counter1()`, increments count to 2

counter2 = counter()  
print(counter2())  # Creates a new `counter` function, starts count at 1

# counter1 is assigned the increment function from the first call to counter(). The count for this instance starts at 0 and is updated with each call.

# counter1() increments count to 1 and returns 1.
# On the second call, count is incremented to 2 and returns 2.
# counter2 is a separate instance of the counter function, so it creates a new count variable.

# The first call to counter2() increments its local count (enclosed in its scope) to 1 and returns 1.
