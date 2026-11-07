price_dict = {"Laptop": 55000,"Phone": 25000,"Headphones": 2000,"Keyboard": 1500,"Mouse": 800,"Monitor": 12000}

print("Product Prices:", price_dict)

price_dict["Tablet"] = 18000

price_dict["Phone"] = 27000

price_dict.pop("Mouse")

product = "Camera"

if product in price_dict:
    print("Price:", price_dict[product])
else:
    print("Product not found")

average_price = sum(price_dict.values())/len(price_dict)

print("Average Product Price:", average_price)