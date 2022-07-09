import random


def guess_number():
    s_num = str(input("Enter start number: "))
    e_num = str(input("Enter end number: "))
    guess = str(input("Enter your guess: "))

    random_number = random.randint(int(s_num), int(e_num))

    if int(guess) == random_number:
        print("You win!")

    else:
        print("You lose!")
        print("The number was", random_number)


guess_number()

yn = str(input("Do you want to play again? (y/n): "))

if yn == "y":
    guess_number()

else:
    print("Bye!")
    exit()

# Code By Pro Gamer 711 YT (BB's Dev)#9546
# Discord Server: https://discord.gg/XwjpcaphZB
