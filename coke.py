def main():
    amount = 50
    dim = [25, 10, 5]
    while amount >0:
        print(f"Amount Due: {amount}")
        coin = int(input("Insert Coin: "))
        if coin not in dim:
            pass
        else:
            amount = amount - coin
    
    print("Take your Coke")

main()