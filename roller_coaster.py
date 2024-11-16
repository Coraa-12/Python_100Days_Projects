def main():
    try:
        age = int(input("Enter your age: "))
        height = int(input("Enter your height in cm: "))
        bill = 0

        if height >= 120:
            print("You are tall enough to ride the roller coaster.")
            if age < 12:
                print("Ticket is $5 for children")
                bill += 5
            elif age < 18:
                print("Ticket is $7 for teenagers")
                bill += 7
            else:
                print("Ticket is $12 for adults")
                bill += 12

            is_photo = input("Do you want a photo for $3? (yes/no): ")

            if is_photo == "yes" or is_photo == "y":
                bill += 3
                print(f"Your final bill is ${bill}")
            else:
                print(f"Your final bill is ${bill}")
        else:
            print("You are not tall enough to ride the roller coaster.")
    except ValueError as e:
        print(f"A ValueError occurred: {e}")


if __name__ == "__main__":
    main()