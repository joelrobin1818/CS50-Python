text = input("Enter name")
size = len(text)
newStr = ""

for i in range(0,size):
    if(text[i].isupper()):
        newStr = newStr + "_" + text[i].lower()
    else:
        newStr = newStr + text[i]

print(newStr)
