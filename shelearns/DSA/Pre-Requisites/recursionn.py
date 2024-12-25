# s=input("ENTER THE STRING TO BE REVERSED :")
# def rev(s):
#     l=len(s)
#     for i in s:
#          n=enumerate(s)
#          n=l-n+1

# print("THE REVERSED STRING IS : ")
# rev()
def rev(s):
   #if single char means same is reverse
    if len(s) <= 1:
        return s
   #for each recursion,first char is separated and the string remains...like this string shrinks adding each starting letter one at a time appended.
    return rev(s[1:]) + s[0]


s = input("ENTER THE STRING TO BE REVERSED: ")
print("THE REVERSED STRING IS:", rev(s))


s = input("ENTER THE STRING TO BE REVERSED: ")
reversed_s = s[::-1]  #slicing:s[start(default to beginning):end(default end):step(start from last character indices wise)]
print("THE REVERSED STRING IS:", reversed_s)
