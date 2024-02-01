def main():
    text = input("Whats the answer to the question: the Great Question of Life, the Universe and Everything?? ")
    if text == "42" or text.lower() == "forty-two" or text.lower() == "forty two":
        print("Yes")
    else:
        print("No")

main()