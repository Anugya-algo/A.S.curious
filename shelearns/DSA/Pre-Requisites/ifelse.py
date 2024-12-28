# Write a Python program that prints numbers from 1 to N. However, for certain numbers, the program should modify the output as follows:

# Replace numbers divisible by 3 with "Fizz". Replace numbers divisible by 5 with "Buzz". Replace numbers divisible by both 3 and 5 with "FizzBuzz". Replace numbers divisible by 7 with "Bang". If a number satisfies multiple conditions, apply all applicable rules in the order given (e.g., a number divisible by 3, 5, and 7 would output "FizzBuzzBang").

def fizz_buzz_bang(n):
    for i in range(1, n + 1):
        output = ""
        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        if i % 7 == 0:
            output += "Bang"
        print(output if output else i)

if __name__ == "__main__":
    
    try:
        N = int(input())
        if 1 <= N <= 105:
            fizz_buzz_bang(N)
        else:
            print("Error: N must be between 1 and 105.")
    except ValueError:
        print("Error: Please input a valid integer.")

