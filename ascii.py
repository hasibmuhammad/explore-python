print("Enter a string: ", end="")

text = input()

for char in text:
    print(char, "\t", ord(char))