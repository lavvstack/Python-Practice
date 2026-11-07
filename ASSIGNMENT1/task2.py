categories = ["electronics", "clothing", "books", "electronics", "home", "beauty"]
categories_set = set(categories)

print("Categories:", categories_set)

categories_set.add("sports")
categories_set.add("books")

print("Electronics available?", "electronics" in categories_set)
print("Number of categories:", len(categories_set))