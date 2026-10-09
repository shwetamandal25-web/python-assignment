
## maing to-do app##



tasks = ["study python", "learn js", "practice DSA", "watch podcast"]

user = int(input("enter the number: "))

if user == 1:
    tasks.append("practice coding")
    print(tasks)

elif user == 2:
    index = int(input("enter the index: "))
    tasks.pop(index)
    print(tasks)

elif user == 3:
    tasks.pop()
    print(tasks)

elif user == 4:
    tasks.sort()
    print(tasks)

elif user == 5:
    print(tasks)

elif user == 6:
    print("Exit the app")

else:
    print("Invalid option")