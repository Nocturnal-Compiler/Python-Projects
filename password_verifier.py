special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '_', '-', '+', '=', '~', '`', '|', '{', '}', ':', ';',
                      '"', '\'', '<', '>', '?', '/', '.', ',']

check_password = input("Enter your password: ")

def password_verifier(password):
    import re
    if len(password) < 8:
        print("Password is too short")
    elif len(password) > 16:
        print("Password is too long")
    elif not re.search("[a-z]", password):
        print("Password must contain at least one lowercase letter")
    elif not re.search("[A-Z]", password):
        print("Password must contain at least one uppercase letter")
    elif not re.search("[0-9]", password):
        print("Password must contain at least one number")
    elif not re.search("[!-:]", password):
        print("Password must contain at least one special character")
    elif re.search("\s", password):
        print("Password must not contain spaces")
    else:
        print("Password is valid")


password_verifier(check_password)

# Code By Pro Gamer 711 YT (BB's Dev)#9546
# Discord Server: https://discord.gg/XwjpcaphZB
