# Library Fine Policy Update##
# Your college library has updated its fine policy for overdue books:
# Standard Books: Charged Rs 5/day for the first 5 days. Any days beyond the 5th day incur Rs 10/day.
# Reference Books: A flat rate of Rs 20/day applies for every overdue day.
# Premium Members: Receive a 20% discount on their total fine
# Library Late Fee Calculator with Tiered Logic
# Implementation Requirements
# Define Function: Design and define a function that calculates and returns the total library fine.
# Parameters & Defaults: Choose required parameters and set appropriate default values (e.g., standard book type, non-premium member).
# Tiered Logic: Construct the tiered conditional logic inside the function body.
# Test Cases: Test your function with diverse combinations of late days, book types, and membership statuses.



def calculation( lateDay, bookType ="standard", premium = False):
    tatalFine = 0
    if lateDay <= 0:
        totalFine = 0

    elif bookType == "standard":

        if lateDay <= 5:
            totalFine = lateDay * 5
        else:
            totalFine = (5 * 5) + ((lateDay - 5) * 10)

    elif bookType == "reference":
        totalFine = lateDay * 20

    else:
        print("Invalid book type")
        return None

    if premium:
        totalFine = totalFine * 0.80

    return totalFine


print(calculation(3))
print(calculation(7))
print(calculation(7, ))
print(calculation(7,  True))
print(calculation(7,  True))
        