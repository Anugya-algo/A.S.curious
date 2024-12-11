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
        continue  # skip printing 3
    if i == 6:
        break  # exit the loop when i is 4
    print(i)
