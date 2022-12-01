import random
import os

numberMax = 1000000
inp = "n"
options = []

for i in range(numberMax):
    options.append(i+1)

os.system("clear")
print("NUMBER GUESSER\n")

print("Think of a number between 1 and " + str(numberMax) + ", I will try to guess it")
input("Press Enter when you are ready...")

i = 0
while(inp[0] == "n"):
    os.system("clear")

    print("NUMBER GUESSER\n")
    choice = random.choice(options)
    print("I think your number is " + str(choice))
    inp = input("Am I right? ").lower()
    while inp == "" or (inp[0] != "y" and inp[0] != "n"):
        inp = input("Please answer Yes or No: ")

    options.remove(choice)
    
    if inp[0] == "n" and len(options) == 0:
        print("You are lying to me, I have already try all the numbers (¬､¬)")
        break
    
    i += 1

if inp[0] == "y":
    if i <= numberMax/4:
        print("That was really easy, you don't even know how to pick a number right")

    elif i <= numberMax/2:
        print("I knew it from the beginning, I was just playing")

    elif i <= numberMax/1.33:
        print("You made me sweat, but don't too happy, you are not that good")

    else:
        print("It took me really long but I it is completely random anyways")

input("\nPress Enter to exit...")
os.system("clear")