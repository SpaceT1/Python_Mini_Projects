menu = {"popcorn": 5.00,
        "soda": 2.00,
        "nacho": 4.00}

total = 0
cart = []

print("------- MENU -------")

for key, value in menu.items():
    print(f"{key:10}: {value:.2f}")

print("--------------------")

while True:
    food = input("select product(press q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("---- YOUR ORDER ----")

for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"total: ${total:.2f}")


