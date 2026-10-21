def total_spent(expenses):
    total = 0

    for expense in expenses:
        total = total + expense[1]

    return total


def biggest_expense(expenses):

    if len(expenses) == 0:
        return None

    biggest = sorted(expenses, key=lambda x: x[1])[-1]

    return biggest

