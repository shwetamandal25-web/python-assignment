# You are writing ticket-booking logic for an IRCTC-style portal. Determine whether a passenger is eligible for a special senior citizen lower-berth preference and a ticket discount.
# The condition is met if the passenger is a senior citizen (age 60 or above) OR a female passenger traveling alone, AND they are booking a non-Tatkal ticket, but only if the journey is not on a blackout festival holiday date.

age = int(input("Enter age: "))
gender = input("Enter gender: ")
alone = input("Are you traveling alone? yes/no: ")
tatkal = input("Is it a Tatkal ticket? yes/no: ")
holiday = input("Is it a blackout holiday? yes/no: ")

eligible = (age >= 60 or gender == "female" and alone == "yes") and tatkal == "no" and holiday == "no"

print( eligible)