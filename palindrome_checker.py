palindrome = input("Enter A String To Check If It Is A Palindrome : ")


def palindromeChecker(string):
    if string == string[::-1]:
        print("The String Is A Palindrome : ", True)
    else:
        print("The String Is A Palindrome : ", False)


palindromeChecker(palindrome)

# Code By Pro Gamer 711 YT (BB's Dev)#9546
# Discord Server: https://discord.gg/XwjpcaphZB
