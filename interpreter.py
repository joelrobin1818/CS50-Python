def main():
    text = input("Expression: ")
    array = text.split(" ")
    val = 0
    if array[1] == '+':
        val = float(array[0]) + float(array[2])
    elif array[1] == '-':
        val = float(array[0]) - float(array[2])
    elif array[1] == '/':
        val = float(array[0]) / float(array[2])
    elif array[1] == '*':
        val = float(array[0]) * float(array[2])
    else:
        print("Wrong Expression")

    print(val)

main()