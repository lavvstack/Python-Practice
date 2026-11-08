orders = [1200, 2500, 800, 1750, 3000]

total_revenue = 0
discounted_orders = 0

print("Order Amount | Discount | Final Amount")

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

    if discount > 0:
        discounted_orders += 1

    print(order_amount, "       |", discount, "%      |", final_amount)

print("\nTotal Revenue After Discounts:", total_revenue)
print("Number of Discounted Orders:", discounted_orders)