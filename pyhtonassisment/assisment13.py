prices = {
    "apple": 50,
    "banana": 30,
    "milk": 60,
    "bread": 40,
    "rice": 100
}

out_of_stock = {"milk", "rice"}

orders = ["apple", "milk", "bread", "banana", "rice"]

total = 0

for item in orders:
    if item in out_of_stock:
        print(item, "is unavailable")
    else:
        total = total + prices[item]

print("Final order value:", total)