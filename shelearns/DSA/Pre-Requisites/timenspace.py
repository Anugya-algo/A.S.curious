# O(1)=CONSTANT TIME; space:index variable
# O(logn)=execution time grows logarithmically with input size; each level recursion
# O(n)=execution time grows linearly with iput size;space check each element
# O(n^2)=grows quadratically

# #SPACE COMPLEXITY
# input space=memory occupied by inputs
# auxiliary space=temporary space during computations


import sys

a=[1,2,3,4,5,]
b=42

print("size: ",sys.getsizeof(a),"bytes")
import tracemalloc

tracemalloc.start()

a=[i for i in range(100)]

current,peak=tracemalloc.get_traced_memory()
print(f"current memory use:{current/1024:.2f}kb")
tracemalloc.stop()