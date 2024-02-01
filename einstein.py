'''
In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms) and then 
outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.
'''

def main():
    c = 3*10**8
    try:
        m = int(input("Enter the mass: "))
        print(f"Energy: {m*c**2} Joules")
    except ValueError:
        print("Enter Integer Value")


if __name__ == "__main__":
    main()