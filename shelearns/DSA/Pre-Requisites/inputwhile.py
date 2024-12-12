user_input = ''
while user_input != 'exit':
    user_input = input("Type 'exit' to stop: ")
    print(f"You typed: {user_input}")



while True:
    user_input=input("Type 'exit ' to stop :")
    if user_input=="exit":
        break#exits the loop
    print(f"You typed {user_input}")

i = 0
while i < 7:
    i += 1
    if i == 3:
        continue  # skip present iteration 3 ko print nhi
    if i == 6:
        break  # when i is 4 exits complete loops
    print(i)
