n=int(input("ENTER A NUMBER TO BE EXAMINED : "))

if n<=1 :
         print("NOT A PRIME NUMBER")
else:
        prime=True#suppose number is prime
        for i in range(2,int(n**0.5)+1):#check till root n
                if n%i==0:#if this is satisfied means got evidence to prime.
                        prime= False
                        break#loop stopped coz we know it is prime no.

if prime:
        print("PRIME NO. ")
else:
        print("NOT PRIME NO.")      




import math

n = int(input("Enter a number to check if it's prime: "))


if n <= 1:
    print("Not a prime number")
elif n == 2:
    print("Prime number")
elif n % 2 == 0:
    print("Not a prime number")
else:
    
    is_prime = True
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            is_prime = False
            break
    
    
    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")





n = int(input("ENTER A NUMBER TO BE EXAMINED: "))

if n <= 1:  
    print("Not a prime number")
else:
    count = 0  
    for i in range(1, n + 1):  
        if n % i == 0:  
            count += 1

    if count == 2:  
        print("Prime number")
    else:
        print("Not a prime number")

