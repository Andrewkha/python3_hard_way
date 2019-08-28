from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want hit CTRL-C")
print("If you want to do it, hit ENTER")

input("?")

print(f"Opening the file {filename}...")
target = open(filename, 'w+')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I will ask you for three lines")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I will write them into file. ")
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

target.seek(0)
print("Here's the new file content:")
print(target.read())

print("And now closing the file")
target.close()

