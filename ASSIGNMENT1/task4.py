catalog = [
    ("Laptop", 55000, "Electronics"),
    ("Phone", 25000, "Electronics"),
    ("Shirt", 1200, "Clothing"),
    ("Jeans", 1800, "Clothing"),
    ("Novel", 500, "Books"),
    ("Notebook", 100, "Books"),
    ("Headphones", 2000, "Electronics")
]

category_to_products = {}

for product, price, category in catalog:
    if category not in category_to_products:
        category_to_products[category] = []

    category_to_products[category].append(product)

print("Category to Products:", category_to_products)

max_category = max(
    category_to_products,
    key=lambda category: len(category_to_products[category])
)

print("Category with max products:", max_category)
print("Products:", category_to_products[max_category])