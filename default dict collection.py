#provides defaut values for missing keys in dict
# Specify a default factory function (e.g., int, list, str) 
# when creating the DefaultDict.

from collections import defaultdict

dd = defaultdict(list)

pairs = [('a', 1), ('b', 2), ('a', 3)]
for key, value in pairs:
    dd[key].append(value)

print(dd) 