print("==============================")
print("     ART SUPPLIES BILLING")
print("==============================")

items = {
    1: ("Pencils", 20),
    2: ("Sketch Pens", 80),
    3: ("Crayons", 60),
    4: ("Paints", 120),
    5: ("Paint Brushes", 50)
}

total = 0

while True:
    print("\nArt Supplies:")
    for number, item in items.items():
        print(number, "-", item[0], "₹" + str(item[1]))
    print("0 - Finish")

    choice = int(input("Choose an item: "))

    if choice == 0:
        break

    if choice in items:
        quantity = int(input("Enter quantity: "))
        name, price = items[choice]
        cost = price * quantity
        total += cost
        print(name, "x", quantity, "=", "₹" + str(cost))
    else:
        print("Invalid choice!")

print("\n==============================")
print("          BILL")
print("==============================")
print("Total Amount: ₹" + str(total))

payment = float(input("Enter payment amount: ₹"))

if payment >= total:
    print("Change: ₹" + str(payment - total))
    print("Thank you for shopping!")
else:
    print("Insufficient payment.")
    print("You still need: ₹" + str(total - payment))