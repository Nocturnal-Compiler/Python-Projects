import datetime

s_date = str(input("Enter start date (example: 2022-7-13): "))
e_date = str(input("Enter end date (example: 2022-7-19): "))

days = (datetime.datetime.strptime(e_date, "%Y-%m-%d") - datetime.datetime.strptime(s_date, "%Y-%m-%d")).days

print("Amount days between", s_date, "and", e_date, "is", days)

# Code By Pro Gamer 711 YT (BB's Dev)#9546
# Discord Server: https://discord.gg/XwjpcaphZB
