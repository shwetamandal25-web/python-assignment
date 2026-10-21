
#    1. Myntra Shopping Discount Cart

# Write a program to calculate an online cart total for 2 fashion items. Ask for item prices using input(), apply a 15% promo code discount, add ₹99 delivery fee, and print an itemized bill.##

item1 = float(input("Enter price of first item: "))
item2 = float(input("Enter price of second item: "))

total = item1 + item2

discount = total * 15 / 100

after_discount = total - discount

delivery_fee = 99

final_amount = after_discount + delivery_fee

print( item1)
print(item2)
print( total)
print( discount)
print( delivery_fee)
print( final_amount)



# Café Outing Split-Bill Calculator

# Build a cafe bill splitter for a hangout with friends. Take total bill amount and number of friends via input(). Cast inputs, add 10% tip, and print how much each person pays.



bill = float(input("Enter total bill amount: "))
friends = int(input("Enter number of friends: "))

tip = bill * 10 / 100

total_bill = bill + tip

each_person = total_bill / friends

print( bill)
print( tip)
print( total_bill)
print(each_person)


# 3. Instagram Reel Engagement Tracker

# Store views (int), likes (int), and comments (int) for a viral reel. Calculate engagement rate percentage: ((likes + comments) / views) * 100. Print a performance audit report.

views = 10000
likes = 1500
comments = 200

engagement_rate = ((likes + comments) / views) * 100

print( views)
print( likes)
print( comments)
print( engagement_rate, "%")


# 4. Monthly Allowance & Savings Planner

# Store monthly pocket money (float) and 3 expense variables (canteen, transport, shopping). Calculate remaining savings, check if is_budget_safe (bool), and print a summary.

pocket_money = float(input("Enter monthly pocket money: "))

canteen = float(input("Enter canteen expense: "))
transport = float(input("Enter transport expense: "))
shopping = float(input("Enter shopping expense: "))

total_expense = canteen + transport + shopping

savings = pocket_money - total_expense

is_budget_safe = savings >= 0


print( pocket_money)
print( canteen)
print( transport)
print(shopping)
print( total_expense)
print( savings)
print( is_budget_safe)


