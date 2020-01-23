fNumber = float(input("Give a decimal number: "))
sNumber = int(input("Give an integer number: "))
power = (fNumber ** sNumber)
print(str(fNumber) + " to the power of " + str(sNumber) +
      " is approximately " + str(round(power)) + ".")
print("To be exact it is " + str(round(power, 2)) + ".")
