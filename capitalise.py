# Write a program that accepts a string as input, capitalizes the first letter of each word in the 
#  string, and then returns the result string.
def capitalize_words(input_string):
    return ' '.join(word.capitalize() for word in input_string.split())

user_input = input("Enter some words: ")
result = capitalize_words(user_input.lower())
print(result)
