text = input("Enter the text: ")
map = ['a','e','i','o','u']
size = len(text)
newStr = ""

for i in range(0,size):
    if text[i].lower() not in map:
        newStr = newStr + text[i]

print(newStr)