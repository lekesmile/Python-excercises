# Write a Python program that asks for two numbers, and prints all the numbers between them, including the numbers themselves. The first number is the lower limit, the second is the upper limit.

# Output should be as follows:

# Give lower limit: 5
# Give upper limit: 10

firstNumber = int(input("Give lower limit: "))
secondNumber = int(input("Give upper limit: "))
for number in range(firstNumber, secondNumber + 1):
    print(number)
