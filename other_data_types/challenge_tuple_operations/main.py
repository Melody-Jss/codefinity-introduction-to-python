# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")
shelf.count("apples")
apple_count = shelf.count("apples")
print("Number of Apples:" , apple_count)

shelf.index("bananas")
banana_index = shelf.index("bananas")
print("First Banana Index:" , shelf.index("bananas"))

if shelf.count("apples") < 5:
    print("Apples need to be restocked.")
else:
    print("Apples are sufficiently stocked.")

shelf.count("grapes")
if shelf.count("grapes") == 1:
    print("Grapes need to be restocked.")
else:
    print("Grapes are sufficiently stocked.")

shelf.index("oranges")
orange_index = shelf.index("oranges")
if "oranges" in shelf:
    print("Oranges are at index:" , orange_index )
else: 
    print("Oranges are out of stock.")