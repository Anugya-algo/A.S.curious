#List comprehension is preparing list from existing list
 
list=['Anugya','Arin','Smita','George']

A_name=[e for e in list if 'A' in e]
#for e in names:
#   if 'A in e:
#      A_name.append(e)

#[(storer for new list) for (entity name) in (list) if (condition) is true]
print(A_name)

animals=['lion'',tiger','monkey','frog']
filtered_animals=[a.title() for a in animals ]
print(filtered_animals)