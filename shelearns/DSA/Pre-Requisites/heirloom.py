#My dear programmer, you are given a string by your grandfather, the King of Eralith, the fallen kingdom of Elves. That string is your family heirloom, you must treasure it and pass it down the line. But now you see a dazzling donut in a bakery unknown, and the cost of the donut is to give the string as a pure offering but alas your string to be treasured forever, has a few characters not so pure, remove them and pass it to the baker or the donut may get lost forever.

#Description: You will be given an impure string and impure characters, you must return a purified string.

# Input Format

# The input will consist of a single dictionary, provided as a string, containing two keys: "string": A string representing the family heirloom. "impure_chars": A list of characters considered impure.

# Constraints

# 1 ≤ number of impure characters ≤ 20 Each impure character is a single printable ASCII character

# Note: The input dictionary keys (string and impure_chars) will always be present. impure_chars will always contain valid characters, and the string will always be printable ASCII.
def purify_string(input_data):
    
    string = input_data['string']
    impure_chars = set(input_data['impure_chars']) 
    purified_string = ''.join([char for char in string if char not in impure_chars])
    
    return purified_string

input_data = {
    "string": "Lets f*&king go, we the elves you %$%$&%",
    "impure_chars": ["*", "%", "$", "&"]
}

print(purify_string(input_data))
