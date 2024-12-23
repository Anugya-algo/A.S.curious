if []:  
    print("This is answe truthy.")
else:
    print("This is falsy")  

a = True
b = False
print(a and b)  
print(a or b)   
print(not a)    

#voting eligiibility

age = input("Enter your age: ")

try:
    age = int(age) 
    if age >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote yet.")
except ValueError:
    print("Invalid input! Please enter a valid number.")


# Truthy/Falsy Evaluation
value = input("Enter a value: ")

if value:  
    print(f"The value '{value}' is truthy.")
else:
    print(f"The value '{value}' is falsy.")

if not value:
    print("Empty strings are considered falsy.")

