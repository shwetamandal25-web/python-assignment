# f = open("diary.txt","w")
# f.write("I like the way you explain concepts.\n")
# f.write("i like you are asking question\n")
# f.write("i like breaks that you gives ")
# f.close()


# f = open("diary.txt", "r")

# data = f.read()

# print(data)

# f.close()


f = open("diary.txt", "w")

f.write("I like the way you explain concepts.\n")
f.write("i like you are asking question\n")
f.write("i  don't like breaks that you gives ")

f.close()


f = open("diary.txt", "r")

data = f.read()

print(data)

f.close()
