# 1. Nested Loops: Prime Numbers

# Write a program to find and print all prime numbers between 2 and 50 using nested loops.

for num in range(2, 51):
    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count = count + 1

    if count == 2:
        print(num)

# 2. Fibonacci Sequence

# Generate the first 10 numbers of the Fibonacci sequence using a while loop and multiple assignment.



a = 0
b = 1
count = 0

while count < 10:
    print(a)

    c = a + b
    a = b
    b = c

    count = count + 1