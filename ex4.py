# Write a program which asks for two numbers. The program should then print "x is larger than y" where x is the larger of the two numbers and y the smaller. If the numbers are equal the program should just say that the numbers are equal.

# The output should be as follows:

# Give the first number: 1
# Give the second number: 2
# 2 is larger than 1

# Give the first number: 2
# Give the second number: 1
# 2 is larger than 1

# Give the first number: 1
# Give the second number: 1
# 1 is equal to 1


firstNum = input("Give the first number: ")
secondNum = input("Give the second number: ")

if firstNum > secondNum:
  print(firstNum + " is larger than " + secondNum)

elif firstNum < secondNum:
  print(secondNum + " is larger than " + firstNum)

else:
  print( firstNum + " is equal " + secondNum)
