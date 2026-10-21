import csv


def save_expenses(expenses):
    with open("expenses.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Item", "Amount"])

        for expense in expenses:
            writer.writerow(expense)


def load_expenses():
    expenses = []

    try:
        with open("expenses.csv", "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                item = row["Item"]
                amount = int(row["Amount"])

                expenses.append((item, amount))

    except FileNotFoundError:
        print("No previous expense file found.")

    return expenses