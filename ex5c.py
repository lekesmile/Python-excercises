# Write a program to keep track of the average of your course grades. (Grades are between 1 to 5.) The program should ask for individual course grades, and calculate the average. An error message should be printed if the grade is out of bounds. -1 will be used as an input to stop the program.

# Output should be as follows:

# Give a course grade(-1 exits): 5
# Give a course grade(-1 exits): 3
# Give a course grade(-1 exits): 1
# Give a course grade(-1 exits): 0
# Grades must be between 1 and 5 (-1 exits)
# Give a course grade(-1 exits): 4
# Give a course grade(-1 exits): -1
# Average of course grades is: 3.2


while True:
    number = input("Give a course grade(-1 exits): ")
    if number < "1" or number > "5 ":
        print("Grades must be between 1 and 5 (-1 exits)")
    else:
        print("Average of course grades is: " + number / len(number))
    break
