orders = []

while True:
    print("\nORDER MENU")
    print("1 - Add Order Amount")
    print("2 - Show All Orders and Total")
    print("q - Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            amount = int(input("Enter order amount: "))
            orders.append(amount)
            print("Order added successfully!")

        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue

    elif choice == "2":

        if len(orders) == 0:
            print("No orders available.")
            continue

        total_revenue = 0

        print("\nOrder Amount | Discount | Final Amount")

        for order_amount in orders:

            if order_amount >= 2000:
                discount = 15
            elif order_amount >= 1500:
                discount = 10
            elif order_amount >= 1000:
                discount = 7
            else:
                discount = 0

            discount_amount = order_amount * discount / 100
            final_amount = order_amount - discount_amount

            total_revenue += final_amount

            print(order_amount, "       |", discount, "%      |", final_amount)

        print("\nTotal Revenue After Discounts:", total_revenue)

    elif choice == "q":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
        continue