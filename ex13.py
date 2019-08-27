from sys import argv

script, first, second, third = argv

print(argv)

user_input = input('Provide one more parameter: ')

print("The script called is:", script)
print("First variable is:", first)
print("Second variable is:", second)
print("Third  variable is:", third)
print("User provided variable is:", user_input)

