def add_price(prices_list, price):
    prices_list.append(price)


def get_average_price(prices_list):
    if len(prices_list) == 0:
        return 0
    return sum(prices_list) / len(prices_list)


def get_max_price(prices_list):
    if len(prices_list) == 0:
        return 0
    return max(prices_list)


prices_list = []

while True:
    print("\n1. Add price")
    print("2. Show average price")
    print("3. Show highest price")
    print("q. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        price = float(input("Enter price: "))
        add_price(prices_list, price)
        print("Price added successfully.")

    elif choice == "2":
        print("Average price:", get_average_price(prices_list))

    elif choice == "3":
        print("Highest price:", get_max_price(prices_list))

    elif choice == "q":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")