def main():
    text = input("What time it is: ")
    convert(text)


def convert(time):
    hr, min = time.split(":")
    if hr == "7": print("Breakfast")
    elif hr == "8" and min == "00": print("Breakfast")
    elif hr == "12": print("Lunch")
    elif hr == "13" and min == "00": print("Lunch")
    elif hr == "18": print("Dinner")
    elif hr == "19" and min == "00": print("Dinner")


if __name__ == "__main__":
    main()