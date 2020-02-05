# Continue with the program in the first exercise. Add the functionality to print the numbers in either ascending or descending order.

# Output should be as follows:

# Give lower limit: 11
# Give upper limit: 20
# Ascending order(yes/no): yes


firstNumber = int(input("Give lower limit: "))
secondNumber = int(input("Give upper limit: "))
question = input("Ascending order (yes/no): ")

for number in range(firstNumber, secondNumber+1):
    if question == "yes":
        print(number)
for number in reversed(range(firstNumber, secondNumber + 1)):
    if question == "no":
        print(number)
