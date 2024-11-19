# roller_coaster2.py
def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Please enter a valid number")


def calculate_bill(height, age, wants_photo):
    bill = 0
    if height >= 120:
        print("You are allowed to ride the roller coaster.")

        if age < 12:
            print("The ticket price is $5 for children")
            bill += 5
        elif age < 18:
            print("The ticket price is $7 for teens")
            bill += 7
        elif 45 <= age <= 55:
            print("The ticket is free for our senior riders")
        else:
            print("The ticket cost $12 for adults.")
            bill += 12

        if wants_photo.lower() in ('yes', 'y'):
            print("Photo added to your bill.")
            bill += 3

        print(f"Your final bill is: ${bill}")
    else:
        print("You are not allowed to ride the roller coaster.")


def main():
    height = get_integer_input("Enter your height in cm: ")
    age = get_integer_input("Enter your age: ")
    wants_photo = input("Do you want a photo for $3 (yes/no): ").strip()
    calculate_bill(height, age, wants_photo)


if __name__ == "__main__":
    main()
