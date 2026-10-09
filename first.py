marks = [50, 70, -10, 90, -20]

sum = 0
count = 0

for num in marks:

    count = count + 1

    if num < 0:
        print("Ignore the number")
        continue

    sum = sum + num

print(sum)
print(count)


## guessing the number game ##
import random

computer_number = random.randint(1, 5)
print(computer_number)

for i in range(3):

    user = int(input("Enter the number: "))

    if user == computer_number:
        print("You guessed it right")
        break

    else:
        print("Wrong guess, try again")
