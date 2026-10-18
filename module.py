# import random
# rand_number=random.randrange(1,10)
# print(rand_number)



## dice game##


from random import randrange
firstDice = randrange(1,6)
secondDice = randrange(1,6)
print(firstDice)
print(secondDice)

total = firstDice+secondDice
print(total)
if(total ==12): 
   print("jackport")