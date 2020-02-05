# Username: Bob
# Password: boB
# Access granted!
# Welcome back, Bob. You have no new mail.
# Username: MattSmith
# Password: CorrectHorseBatteryStaple
# User not recognized, please try again!
# Username: Bob
# Password: not_bob
# Wrong password!

username = input("Username: ")
password = input("Password: ")

defUsername = "Bob"
defPassword = "boB"

if username == defUsername and password == defPassword:
    print("Access granted!")
    print("Welcome back, " + username + ". You have no new mail.")

elif username == defUsername and password != defPassword:
    print("Wrong password!")

if username != defUsername:
    print("User not recognized, please try again!")
