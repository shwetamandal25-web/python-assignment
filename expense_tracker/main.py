from storage import save_expenses, load_expenses
from reports import total_spent, biggest_expense


expenses = load_expenses()

print(" EXPENSE TRACKER ")

for i in range(3):

    item = input("Enter expense item: ")

    try:
        amount = int(input("Enter amount: "))

        expenses.append((item, amount))

    except ValueError:
        print("Please enter a valid number.")
        continue


save_expenses(expenses)

total = total_spent(expenses)
biggest = biggest_expense(expenses)


print("\nREPORT")

print("Total spent:", total)

if biggest is not None:
    print("Biggest expense:", biggest[0], "-", biggest[1])
else:
    print("No expenses available.")