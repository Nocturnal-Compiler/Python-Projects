def password_generator(length):
    import random
    import string
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))


pass_length = int(input("Enter the length of the password: "))

print("Your password is:", password_generator(pass_length))

# Code By Pro Gamer 711 YT (BB's Dev)#9546
# Discord Server: https://discord.gg/XwjpcaphZB
