# Do you know how to calculate a dog's equivalent age in human years? It is commonly thought that a year of a dogs life is equivalent to 7 human years, but this is in fact not true...

# According to American Kennel Club:

# 15 human years equals the first year of a medium-sized dog’s life.
# Year two for a dog equals about nine years for a human.
# And after that, each human year would be approximately five years for a dog.
# Write a program that converts a dog's real age in years to the equivalent human years. If the dog is 0 years old, the program should print "A 0 years old dog is still a puppy, but up to 15 years old in human age!" Otherwise, the program should print"A X year old dog is about Y years old in human age."

# The output should be as follows:

# How old is the dog?: 1
# A 1 year old dog is about 15 years old in human age.
# How old is the dog?: 3
# A 3 year old dog is about 29 years old in human age.
# How old is the dog?: 5
# A 5 year old dog is about 39 years old in human age.
# How old is the dog?: 0
# A 0 years old dog is still a puppy, but up to 15 years old in human age!


# fMessage = int(input("How old is the dog?: "))
# humanAge = 15

# if fMessage == 0:
#     print("A " + str(fMessage) +
#           " years old dog is still a puppy, but up to 15 years old in human age!")
# elif fMessage == 1:
#    print("A " + str(fMessage) + " year old dog is about " +
#         str(humanAge) + " years old in human age.")
# elif fMessage == 2:
#     print("A " + str(fMessage) + " year old dog is about " +
#           str(humanAge + 9) + " years old in human age.")
# elif(fMessage == 3):
#     print("A " + str(fMessage) + " year old dog is about " +
#          str(24  + 5 ) + " years old in human age.")
# elif(fMessage == 4):
#     print("A " + str(fMessage) + " year old dog is about " +
#          str(24  + 5 + 5 ) + " years old in human age.")
# elif(fMessage == 5):
#     print("A " + str(fMessage) + " year old dog is about " +
#           str(24 + 5 + 5 + 5) + " years old in human age.")


dog_age = int(input("How old is the dog?: "))

human_age = 0

if dog_age > 0:  # the dog is at least 1 year old
    human_age = human_age + 15

    if dog_age > 1:  # the dog is at least 2 years old
        human_age = human_age + 9

        if dog_age > 2:  # dog is 3 years or older
            human_age = human_age + (dog_age-2) * 5

if dog_age == 0:
    print("A 0 years old dog is still a puppy, but up to 15 years old in human age!")
else:
    print("A", dog_age, "year old dog is about",
          human_age, "years old in human age.")
