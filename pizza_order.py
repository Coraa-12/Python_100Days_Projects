def calculate_total(size: str, pepperoni: str, cheese: str):
    price = 0

    if size == "S" or size == "s":
        price += 15
    elif size == "M" or size == "m":
        price += 20
    else:
        price += 25

    if pepperoni == "Y" or pepperoni == "y":
        if size == "S" or size == "s":
            price += 2
        else:
            price += 3
    else:
        pass

    if cheese == "Y" or cheese == "y":
        price += 1
    else:
        pass

    return price

def main():
    size = input("Enter the size of the pizza (S, M, L): ")
    pepperoni = input("Do you want pepperoni? (Y, N): ")
    cheese = input("Do you want extra cheese? (Y, N): ")

    total = calculate_total(size, pepperoni, cheese)
    print(f"Total price: ${total}")


if __name__ == "__main__":
    main()
